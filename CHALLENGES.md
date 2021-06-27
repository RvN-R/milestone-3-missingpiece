* I've used wtfform.validator to incorporate some defensive programming into my project. validators like StringField, PasswordField and Length. Although these work and prompts are appearing asking for the correct information the form is stil submitting to MongoDb. For example I've sent a username minium length of 8 characters, in inputted Jack into this field and inputed 1234 into the password field. the error message came back but as you can see Jack was still submitted to the db. 

Input ISSUE 1 image
Input ISSUE 2 image

I manage to get passed this by using an "and". Now when the function recieves a POST and teh validators are met then the registration us submitted to my DB. Now if my validators aren't met I don't get incorrect information being submitted to my DB, and if a username has already been used then it can't be used again. 

Input ISSUE 3 image

* I struggled to get only the users inventory to appear on the my inventory page. At the moment I could get all of the inventories by all of the users to appear, as seen in the image below: 

Input ISSUE 4 image and Input ISSUE 5 image

To fget passed this issue I released that I had to include an if jinja statement within the jinja for look that was rendering the entire inventory from Mongodb. if session.user was equal the the same user that created the inventory (inventory.created_by) then only there inventory would render. 
