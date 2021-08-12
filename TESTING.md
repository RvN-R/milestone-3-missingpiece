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

## Testing User Stories from UX section in README

### Testing First Time Visitor Goals

1. <b>As a First Time Visitor, I want to easily understand the main purpose of the site, and learn more about the company.</b></br>

* The "About Us" section features 4 paragraphs explaining the companies values, with a main hero image used as a banner on all pages to reinforce those connotations.

2. <b>As a First Time Visitor, I want to be able to easily navigate through the site to find key content.</b></br>

* At the top of each page is a navigation bar that runs the length of the page. Its always at the top of the page and allows the visitor no matter where they are on the website to know the location of the navigation bar. 

3. <b>As a First Time Visitor, I want to clearly find out how to search the database for possible avalaible equipment.</b></br>

* There are two ways for a visitor to search the Missing Piece database. Firstly on the "Home" page (initial page the visitor will arrive at) when they scroll down the page they will arrive at the "So How Does This Work?" section. This section amoungst many other functions clearly explains how the visitor can search the database. It also provides a call to action button labelled "Search Inventory" with spy glass icon, which sends the visitor to the "Search Inventory" page. Alternativley at the top of every page is the navigation bar that can help direct the visitor to the "Search Inventory" page. 

4. <b>As a First Time Visitor, I want to clearly find out how to register an account with the website.</b></br>

* There are two ways for a visitor to register an account on the website.Firstly on the "Home" page (initial page the visitor will arrive at) when they scroll down the page they will arrive at the "So How Does This Work?" section. This section amoungst many other functions clearly explains how the visitor can register an account on the website. It also provides a call to action button labelled "Create Account", which sends the visitor to the "Register" page. Alternativley at the top of every page is the navigation bar that can help direct the visitor to the "Register" page.

5. <b>As a First Time Visitor, I want to source information that validates the organisation's legitimacy. For example, are they a respected company within the UK Live Sound Community.</b></br>

* At the bottom of every page is the footer the visitor will find three social media icons. These three icons will link the visitor all of the Missing Piece social medias. The sites open up in a different tab, so the visitor can continue their journey though the website without being diverted to a different website.However, they should also confirm the validity of the Missing Piece withing the UK Live Sound Community. 

### Testing Returning Visitor Goals

1. <b>As a Returning Visitor, I want to be able to navigate to the search page quickly.</b></br>

* The navigation bar spans with the width of the top of every page, and has a link to the "Search Inventory" page allowing a visitior to navigate there quickly. Alternativley the "So How Does This Work?" section has a button labelled "Search Inventory" that links the visitor to the "Search Inventory" page. 

2. <b>As a Returning Visitor, I want to be able to log in to my account quickly</b></br>

* At the top of every page the visitor will see a navigation bar that spans with width of the top of every page. In the navigation bar they should see "Log In", once clicked it will send them to the "Log In" page. Providing they have previously registered an account on the site they will be able to log in. 

3. <b>As a Returning Visitor, I want to be able to register an account quickly</b></br>

* At the top of every page the visitor will see a navigation bar that spans with width of the top of every page. In the navigation bar they should see "Register", once clicked it will send them to the "Register" page and a form will appear. Once filled out and providing the informatiom meets the form validators requirements, they can click the "Submit" button to register an account. 

4. <b>As a Returning Visitor, I want to be able upload my inventory to my account easily.</b></br>

* Once a visitor has registed or logged into there account in the navigation bar at the top of the screen, a option entitled "Add to Inventory" will appear. Once clicked it takes the visitor to the "Add to Inventory" page. The page has a form with a drop down select component and three text inputs. The form will promopt the visitor to choose a category from the drop down list, input the brand name, product name and quantity of the said product they have in there rental inventories, that they want to advertise on the Missing Piece website. Once the form has been filled out, and form validators met then the visitor can click the call to action button at the bottom of the page entitled "Add to Inventory" and the inventory entry will be uploaded to the site. 

5. <b>As a Returning Visitor, I want to be able to see what inventories I have already uploaded to my account.</b></br>

* Once a visitor has registed or logged into there account in the navigation bar at the top of the screen, a option entitled "My Inventory" will appear. Once clicked it takes the visitor to the "My Inventory" page. On the page the visitor will see any and all inventory entries they have made to the site up until that point. 

6. <b>As a Returning Visitor, I want to be able to see what address information I have linked to my profile.</b></br>

* Once a visitor has registed or logged into there account in the navigation bar at the top of the screen, a option entitled "Profile" will appear. Once clicked it takes the visitor to the "Profile" page. On the page the visitor will see all of the company information they submitted when they registered an account with the site including address informatiom. 

### Testing Frequent Visitor Goals

1. <b>As a Frequent User, I want to be able to navigate to the search page quickly.</b></br>

* The navigation bar spans with the width of the top of every page, and has a link to the "Search Inventory" page allowing a visitior to navigate there quickly. Alternativley the "So How Does This Work?" section has a button labelled "Search Inventory" that links the visitor to the "Search Inventory" page. 

2. <b>As a Frequent User, I want to be able to edit my inventories that I have uploaded to my account. </b></br>

* Providing a visitor has registered or logged into there account, in the navigation bar at the top of the screen, an option will appear entitled "My Inventory". Once clicked they will be taken to a page that displays all the inventory entires they have made up until that point. Each entry is displayed in a card and each card has two buttons entitled "Edit" and "Delete". Once the visitor clicks "Edit" a page will appear indentical to that of the "Add To Inventory" page, but the select and text input elements will be autofilled by the information from said inventory entry. The visitor can edit the information on the form and then click the "Confirm Edit" button. Those changes will be made to that inventory entry, and will appear changed in there "My Inventory" page. 

3. <b>As a Frequent User, I want to be able to delete my inventories that I have uploaded to my account.</b></br>

* Providing a visitor has registered or logged into there account, in the navigation bar at the top of the screen, an option will appear entitled "My Inventory". Once clicked they will be taken to a page that displays all the inventory entires they have made up until that point. Each entry is displayed in a card and each card has two buttons entitled "Edit" and "Delete". Once the visitor clicks "Delete" a Modal warning will appear asking the visitor if they really want to delete this inventory entry. If they click "Yes" then the entry will be deleted, if they click "No" they will be taken back to the "My Inventory" page.

4. <b>As a Frequent User, I want to be able to edit my companies address details.</b></br>

* Once a visitor has registed or logged into there account in the navigation bar at the top of the screen, a option entitled "Profile" will appear. Once clicked it takes the visitor to the "Profile" page. On the page the visitor will see all of the company information they submitted when they registered an account with the site including address informatiom. Just below taht information is a button entitled "Update Info", once clicked they will be transported to a page that looks very similar to the registration form they filled out on the "Registration" page. The form will be autofilled with the most up to date information at the time that they last submitted. The visitor can amend that information, and once they click update there company information will be updated to the database. 

5. <b>As a Frequent User, I want to be able upload my inventory to my account easily.</b></br>

* Once a visitor has registed or logged into there account in the navigation bar at the top of the screen, a option entitled "Add to Inventory" will appear. Once clicked the visitor will be transported to the "Add to Inventory" page, with a form containing a one select and three text input components. The visitor will be prompted to choose a category for the select drop down menu, fill in the brand name of the equipment, the product name and the quantity that they have in there rental inventory. Providing all the elements of the form are filled out, the visitor can click the "Add to Inventory" button and there inventory entry will be uploaded to the database. Once uploaded the "Add to Invenotry" page refreshs and the visitor can repeat the process as many times as they would like. 