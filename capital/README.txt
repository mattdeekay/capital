Updated: Wed, June 1, 2016
Creator: Matthew Kim

Words of Caution
################
1. "Blog" app is not ready and is not called by capital/settings.py to do anything. In the future, it can be repurposed to accept feedback forms from clients.

2. The app "Invite" houses the user authentication framework as requested by Coefficient Capital. However, invite is still in development and is not ready for production-quality deployment.

3. Two-factor authentication packages are installed but are not in use currently.


Description of "Invite" app
###########################
The end goal is for users with an access code to be able to create an account and see "/lastpage.html" which will link to an investor slide deck. For now, the link points back to the homepage of the site.

Home > Access
A visitor is automatically an "AnonymousUser" user by Django specifications. The visitor can try to make an account or view an existing account by clicking on "Access" in the top menu bar of the homepage.

Access options
1. If the user supplies a faulty email, 


