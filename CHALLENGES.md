* I've used wtfform.validator to incorporate some defensive programming into my project. validators like StringField, PasswordField and Length. Although these work and prompts are appearing asking for the correct information the form is stil submitting to MongoDb. For example I've sent a username minium length of 8 characters, in inputted Jack into this field and inputed 1234 into the password field. the error message came back but as you can see Jack was still submitted to the db. 

Input ISSUE 1 image
Input ISSUE 2 image

I manage to get passed this by using an "and". Now when the function recieves a POST and teh validators are met then the registration us submitted to my DB. Now if my validators aren't met I don't get incorrect information being submitted to my DB, and if a username has already been used then it can't be used again. 

Input ISSUE 3 image

* I struggled to get only the users inventory to appear on the my inventory page. At the moment I could get all of the inventories by all of the users to appear, as seen in the image below: 

Input ISSUE 4 image and Input ISSUE 5 image

To get passed this issue I released that I had to include an if jinja statement within the jinja for look that was rendering the entire inventory from Mongodb. if session.user was equal the the same user that created the inventory (inventory.created_by) then only there inventory would render. 

I wanted to add some defensive programming to my site when a user came to delete an inventory from there inventory libary. The best way of doing this would be a modal. When you clicked "Delete" button a modal would pop up making sure you really wanted to do this. After much trial and error I managed to get the "Delete" button to trigger the modal, but when I did there was some obivious CSS issues as you can see in the image below: 

Input ISSUE 9 Image

To get passed this I used some CSS positioning to make the card elements static, this would bring them to the back of the web page and allow the modal to stand out in front. As you can see from the two images below this solved my issue: 

Input ISSUE 10 image 
Input ISSUE 11 image