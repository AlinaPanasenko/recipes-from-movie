![CI logo](https://res.cloudinary.com/dso5orboe/image/upload/v1680100192/project_board_12.03.2023_ocwxai.png)

Welcome AlinaPanasenko,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Errors
When I tried to create restrictions for creating posts for the unregistered user,  I tried to use @login_required decorator first but got an error that indicated that I couldn't use this decorator with class objects. That's why I use LoginRequiredMixin mixin instead.
From here:
https://docs.djangoproject.com/en/4.1/topics/auth/default/
