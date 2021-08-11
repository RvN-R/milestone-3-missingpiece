# Testing

## Testing client Requirements featured in README
* <b>We need a platform that illustrates and shares our key values</b></br>

No matter what section of the site the visitor is currently inhabiting, they have the ability to navigate to the "Home" page using the navigation bar that has the "About Us" section. The "About Us" section contains key information and explains the Missing Pieces key values and point of existance. 

* <b>We need a platform that succinctly explains who we are and the function of the company.</b></br>

When a vistor first arrives the first page they arrive at is the "Home" page that includes both the websites "About Us" and "So How Does This Work?" section. Both sections provide information on the company and how the websites function. 

* <b>We Need a platform that succinctly explains how use the website key functions, that of searching the database or uploading there production inventories.</b></br>

The "So How Does This Work?" section explains in great detail the two main functions of the site, by dividing the main users of the site into two categorys those "Searching" and those wanting to "Advertise" there rental inventories. To increase the effectiveness of this section key words are in bold and icons have been used. Theres also two call to action buttons that direct the vistor to either the "Search Inventory" page or the "Register" page. 

* <b>We need a platform that allows those visiting to register an account with us.</b></br>

The website offers two methods of registering an account, the quickest would be to click the "Register" in the navigation bar at the top of the page, or toggle to the remote view navigation bar if they are looking at the site on a mobile device. Alternatively, when the vistior reads the "So How Does This Work?" section on the "Home" page, they will be see a call to action button called "Create Account" which will also direct them to the "Register" page. 

* <b>We need a platform that allows those who have registered an account to log in and log out freely.</b></br>

Once a visitor successfully fills out the registration form on the "Register" page they will be directed to there "Profile" page and be logged in. If they want to log out then they can click "Log Out" which can be found at the top of the page in the navigation bar. Once clicked the visitor will be logged out, but also be automatically directed back to the "Log In" page. Should they want to log in at a later date they can click the "Log In" in the navigation bar at the top of the page to log back into there account. 

* <b>We need a platform that allows those who have registered to upload there production inventories to the websites database. To be able to edit, or delete inventories once uploaded.</b></br>

Once a visitor has successfully registered an account on the website, or when they successfully log in they are automatically taken to there "Profile" page. From there using the navigation bar at the top of the page the visitor can go to there "Add to Inventory" page. On that page the visitor can fill out the "Add to Inventory" form and that inventory entry will be uploaded to the database. Once uploaded the visitor can go to there "My Inventory" page to see what inventory entries they have uploaded to the database thus far. I've used Materalized Cards to display all of these inventory entries. Each card has two buttons "Edit" and "Delete" allowing the visitor to edit or delete said entry.  

* <b>We need a platform that informs a user what inventories they have already uploaded.</b></br>

Once a visitor has successfully registered an account on the website, or when they successfully log in they are automatically taken to there "Profile" page. From there using the navigation bar at the top of the page the visitor can go to there "My Inventory" page. This page will display all that visitors inventory entries. 

* <b>We need a platform that allows a user to upload there companies contact information, in order for companies searching the database to contact they relating to there inventories.</b></br>

When a visitor registers an account on the website they are prompted to not only include a username and password, but also Company Name, Street Name, Postcode, City Name and finally Phone Number. Once uploaded to the database the Search Function I have written in Python iterates over both the "user" database that holds all of the company information, and the "inventory" database. So when visitors search the Missing Piece database on the "Search Inventory" page, not only does inventory entries that match the search appear, but also the company contact information relating to said inventory entries. 

* <b>We need a platform that allows a user to edit there contact information once uploaded to our database.</b></br>

Once a visitor has successfully registered an account on the website, or when they successfully log in they are automatically taken to there "Profile" page. The page displays the visitors companies information and just below that information is a call to action button labelled "Update Info". Once clicked an indentical page to the "Register" page appears, with all of the current company information pre loaded into the form. The visitor is then able to either edit that information and click the "Update" button to update the company information. Alternatively if the visitor decides not to update the information, they can click the "Cancel" button to take them back to there "Profile" page without editing there information. 
