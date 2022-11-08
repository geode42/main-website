---
name: How this website works
---

When you visit a page on this website, your browser is sent the page's HTML file (and maybe the CSS), and then your browser displays that HTML and CSS. This website is a *static-site*, meaning no JavaScript trickery or anything is going on.

To generate a site like this, many people use something called [Hugo](https://gohugo.io/). Hugo is an open-source static site generator written in [Go](https://go.dev/), meaning it's really fast.

Now, I tried to use Hugo, I really did. *But...* any tutorial or guide I found on it wasn't that helpful, and I kept running into annoyances with it. So, I did what any normal person would do, and completely recreated it.

Okay, fine, I didn't *completely* recreate it. My static site generator has no where near the feature set of Hugo. But the thing is... it doesn't need to have it. Hugo is made for anyone, my thing is made for myself. As such, I only need to implement what I need, and nothing else. This let me write my generator in a fairly short amount of time.


Now obviously my static site generator is no where near as good as Hugo, but the thing is, it doesn't need to be. My static site generator only needs to do what I need it to do for my website, and nothing else. As such, it really didn't take long to make, and allows me the flexibility of being able to do anything I want, rather than figuring out how to work around it in Hugo.

