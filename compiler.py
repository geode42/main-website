import markdown
from os import path, listdir, mkdir
from distutils.dir_util import copy_tree
from dataclasses import dataclass
from typing import List

def compile(src, dist, template, resources):
	# Init markdown object (this reminds me of Java. I don't like Java.)
	md = markdown.Markdown(extensions=['meta'])

	# Get template
	with open(template) as f:
		templatetext = f.read()

	# File dataclass (ironic given I said I don't like Java, I know)
	@dataclass
	class File:
		name: str
		contents: str
		filename: str

	# This list will contain all of the File objects
	files: List[File] = []

	# Populate the list
	srcfiles = listdir(src)
	srcnames = [path.splitext(i)[0] for i in srcfiles]
	for file, filename in list(zip(srcfiles, srcnames)):
		with open(path.join(src, file)) as f:
			contents = f.read()
		compiled_html = md.convert(contents)
		name = filename
		if 'name' in md.Meta:
			name = md.Meta['name'][0] # For some reason md.Meta['name'] returns a list containing one item, weird
		files.append(File(name, compiled_html, filename + '.html'))

	for file in files:
		# Create nav
		nav_elements = []
		for nfile in files: # nav... file? idk what to do in these kinds of situations
			if nfile == file:
				nav_elements.append(f"<li class='current-location'><a href={nfile.filename}>{nfile.name}</a></li>")
			else:
				nav_elements.append(f'<li><a href={nfile.filename}>{nfile.name}</a></li>')
		nav = '\n'.join(nav_elements)


		with open(path.join(dist, file.filename), 'w') as f:
			f.write(templatetext.replace('{{nav}}', nav).replace('{{main}}', file.contents))
	
	# Throw in everything from the resources directory

	if not path.isdir(path.join(dist, 'resources')):
		mkdir(path.join(dist, 'resources'))
	copy_tree(resources, path.join(dist, 'resources'))

compile('src', 'dist', 'template.html', 'resources')