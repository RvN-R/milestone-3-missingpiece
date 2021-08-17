# Testing

I used <a href="https://validator.w3.org/">Markup Validator Service</a>, <a href="https://jigsaw.w3.org/css-validator/">CSS Validator</a>, <a href="https://jshint.com/">JSHint</a> and <a href="http://pep8online.com/">PEP8 Online</a> to check both HTML, CSS, Javascript and Python using the direct input services of both services. The HTML validator doesn't recognised Jinja formatting, so that will come back as and error. However, apart from those results no other issues where flagged.

I used Chrome's inspect feature Lighthouse on my page, to improve the site's performance. The report found the following:

* <b>Performance</b> - Scored 82 for Desktop and 71 for Mobile - The main points of criticism were "Largest Contentful Paint". I was expecting that the creative decision to have a large image within the header would cause the website to score low when it came to load time. Following the test I experimented with different codecs and replaced a number of PNG's with compressed JPEG's in an attempt to improve this score. 

* <b>Accessibility</b> - Scored 89 respectively for both Desktop and Mobile - The test flagged up small issues like "Heading elements are not in a sequentially-descending order" and "Links do not have a discernible name". However, all of these comments do not negatively impact the overall performance of the site. They are linked to creative decisions used to prioritise the aesthetic design by positioning the navigation bar at the top of the header, and using Font Awesome icons as an alternative to text in the social media footer links.

* <b>Best Practices</b> - Scored 87 respectively for both Desktop and Mobile - Another high scoring section of the Lighthouse test, two significant suggestion flagged was "Links to cross-origin destinations are unsafe" and "Does nto use HTTPS". Regardin the first point when you link to a page on another site using the target="_blank" attribute, you can expose your site to performance and security issues. It's suggested to use "<rel="noopener">" in the social media icon links. With regard to HTTPS comment that is more conerning and before presenting the finished product to the end client this would need to be amended. To do that I would need contact a certifaction authority and request a HTTPS certification.

* <b>SEO</b> - Scored 90 for Desktop and 89 for Mobile - Again another high scoring section of the Lighthouse test, and only received limited suggestions, none of which were applicable to the improved running of the site.

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

## Manually Testing Website Features
### Navigation
* Load the Website. 
* Right click and select inspection.
* Change the screen size from desktop to tablet, then change from tablet to smaller devices and verify that the navigation bar is responsive. 
* Confirm that the text in the navigation buttons is unrestricted by differing screen sizes. 
Verify that small screen sizes activate the toggle feature, activating the navigation bar remote view nav button. 
* Click each link in turn and confirm that you are transported to the relative section of the website.
* Confirm that the hover function is operational. 
* Return to desktop view and hover over the navigation links, make sure the hover selection function works for each link. 
* Click each link and make sure you are transported to the correct section of the site. 
* Repeat verification of functionality and responsiveness on iPhone and iPad.

### Home
* Load the Website. 
* Right click and select inspection. 
* Scroll down the page to "About Us" section. 
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy text is appearing as designed. 
* Scroll down the page to "So How Does This Work?" section. 
* Repeat steps above for changing screen sizes, to check sections responsiveness. Text and Buttons should remain visable and be unrestricted. 
* Hover over call to action buttons for both "Search Inventory" and "Create Account", confiming the hover function works properly. When hovered over buttons should go from yellow to black, text should perform the opposite. 
* Perform the following manual check <b>HOME > CLICK "Search Inventory" BUTTON</b> you should be transported to the "Search Inventory" Page. 
* Perform the following manual check <b>HOME > CLICK "Create Account" BUTTON</b> you should be transported to the "Register" Page. 

### Register
* Load the Website.
* Right click and select inspection. 
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy form and all of its attributes are appearing as designed.
* Using either the navigation bar or remote view navigation bar <b>CLICK "Register"</b>. You should be transported to the "Register" page. 
* Scroll down the page and perform the following manual check <b>REGISTER > CLICK "Submit"</b> you should recieve the following prompt above the username field "Please fill in this field". 
* Fill in the username field and <b>CLICK "Submit</b>, you should recieve the following prompt above the password field "Please fill in this field".
* Work down the rest of the form, and perform the follwing manual check one field at a time.
* <b>CLICK FIELD > CLICK "Submit"</b> line below the filed should turn red. Fill in field and the line below the field should turn green. <b>CLICK "Submit</b>, you should recieve the following prompt above the password field "Please fill in this field".
* Before you get to the last field "Phone Number" make sure you have filled out the form with the following test information and <b>CLICK "Submit</b>: 
    * <i>Username</i>: Jack
    * <i> Password</i>: Jack12345
    * <i>Company Name</i>: Jacks Sound Systems 
    * <i>Street Name</i>: Jack Street
    * <i>Postcode</i>: J12 3SL
    * <i>City Name</i>: Bristol
    * <i>Phone Number</i>: 020 8888 8888
* The page should refresh, all of the fields be refreshed and a validator below the username field that says "Username must be between 10 and 15 Characters"
* Fill out the registration from with the following informaiton and <b>CLICK "Submit</b>:
    * <i>Username</i>: JackSoundSystem
    * <i> Password</i>: Jack12345
    * <i>Company Name</i>: Jacks Sound Systems 
    * <i>Street Name</i>: Jack Street
    * <i>Postcode</i>: J12 3SL
    * <i>City Name</i>: Bristol
    * <i>Phone Number</i>: 020 8888 8888
* The page should refresh and you should see a flash message running across the width of the screen saying "Registration Successful Jacks Sound System!"
* Below the flash message you should see a heading that says "Jacks Sound Systems Profile" 
* Below the heading you should see a card with the title "Company Address", which should contain all of the company information you just registered with.
* Depending on the screen size you are currently viewing the site on, navigate to the navigation bar either at the top of the page or toggle to the remote view navigation bar. The bar should have the following links displayed, "Home", "Profile", "Log Out" "Search" Inventory" "Add to Inventory" and "My Inventory"
* Perform the following manual check <b>CLICK "Log Out"</b> link in the navigation bar. 
* Once clicked the website should refresh, a flash message should appear saying "You have been logged out" and you will have been transfered to the "Log In" page. 
* Using the navigation bar or remote view navigation bar and perform the following manual check <b>CLICK "Register"</b>. 
* Fill out all registration form with the same information that you registered with and <b>CLICK "Submit</b>, for a reminder I have included it below: 
    * <i>Username</i>: JackSoundSystem
    * <i> Password</i>: Jack12345
    * <i>Company Name</i>: Jacks Sound Systems 
    * <i>Street Name</i>: Jack Street
    * <i>Postcode</i>: J12 3SL
    * <i>City Name</i>: Bristol
    * <i>Phone Number</i>: 020 8888 8888
* The page will refresh and a flasy message will appear saying "Username already exists. 
* Scroll down to the bottom of the page, below you "Submit" call to action button you should see an anchor link which says "Already Registered ? Log In" and perform the following manual check <b>CLICK "Log In"</b>. You should be transported to the "Log In" page. 

### Logout
* Load the Website. 
* Right click and select inspection.
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy form and all of its attributes are appearing as designed.
* Using either the navigation bar or remote view navigation bar <b>CLICK "Log In"</b>. You should be transported to the "Log In" page. 
* You should see a form with two text inputs, and a call to action button labelled "Log In". 
* Perform the following manual check <b>CLICK "Log In"</b>, you should recieve the following prompt above the username field "Please fill in this field".
* Fill in the username field with the following and <b>CLICK "Log In"</b>: 
    * <i>Username</i>: Jack
* You should recieve the following prompt above the password field "Please fill in this field".
* Fill in the username field with the following and <b>CLICK "Log In"</b>: 
    * <i>Password</i>: password.
* The page will refresh, the form fields will also refresh and a flash message appear saying "Incorrect Username and / or Password". 
* Scroll down to the bottom of the page, below you "Submit" call to action button you should see an anchor link which says "New Here? Register Account" and perform the following manual check <b>CLICK "Register Account"</b>. You should be transported to the "Register" page.
* Using either the navigation bar or remote view navigation bar <b>CLICK "Log In"</b>. You should be transported to the "Log In" page. 
* Using the information you previously used to register an account on the website, fill out the form with the following information and <b>CLICK "Log In"</b>: 
    * <i>Username</i>: JackSoundSystem
    * <i> Password</i>: Jack12345
* You will be transported to Jacks Sound System's Profile page, you will see a flash message that says Welcome, JackSoundSystem. 

### Edit Company Address
* Load the Website. 
* Right click and select inspection.
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy form and all of its attributes are appearing as designed.
* Using either the navigation bar or remote view navigation bar <b>CLICK "Log In"</b>. You should be transported to the "Log In" page.
* Using the information you previously used to register an account on the website, fill out the form with the following information and <b>CLICK "Log In"</b>: 
    * <i>Username</i>: JackSoundSystem
    * <i> Password</i>: Jack12345
* Now you should be transported to JackSoundSystem's profile page. 
* Scroll down the page and <b>CLICK "Update Info"</b>
* The page will refresh and you should see the title "Edit Company Address" and below that will be a form with the title "Input Company Details"
* Scroll down the page and <b>CLICK "Update Info"</b>, you will be transported back to the "Edit Company Address" page.
* You will see a from prefilled in with current company details.
* Change the city name text input from "Bristol" to "London" <b>CLICK "Cancel"</b>,you should be transported back to the "Profile" page. City name should still be Bristol, as you cancelled the edit. 
* Scroll down the page and <b>CLICK "Update Info"</b>, you will be transported back to the "Edit Company Address" page.
* You will see a from prefilled in with current company details.
* Delete "Bristol" from the city name field, <b>CLICK "Update"</b>, you should get a prompt saying "Please fill in this field". 
* Repeat this process with all the fields, to make sure you can't submit the form without filling in all of input fields. 
* Make sure all fields contain the same original company details that you registered the account with. Replace the city name field with "London" and <b>CLICK "Update"</b>
* The "Profile" page will refresh and you should see that the edit you made to the company information will appear within the Company Address card. 

### Add Inventory
* Load the Website. 
* Right click and select inspection.
* Follow the Log In steps to log into JackSoundSystem profile. 
* Using either the navigation bar or remote view navigation bar <b>CLICK "Add to Inventory"</b>. You should be transported to the "Add Inventory" page.
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy form and all of its attributes are appearing as designed.
* When you arrive at the "Add Inventory" page you will see a title that says "Add Inventory" and a sub heading saying "Fill out information below to add to your inventory". 
* Below that you will notice a form, containg a select field and three text input fields. 
* Scroll down the page and <b>CLICK "Add To Inventory"</b>, you should get red line just below the Category field and a a prompt that says "Please select an item in the list". 
* Perform the following manual check <b>SELECT "Monitors"</b> from the select drop down menu. 
* Scroll down the page and <b>CLICK "Add To Inventory"</b>, you should get a prompt just below the Brand Name field that says "Please fill in this field". The line underneath that field should go red. 
* Fill in the field with the following information and the line underneath that field should go green, <b>CLICK "Add To Inventory"</b>:
    * Martin Audio
* You should get a prompt just below the Product Name field that says "Please fill in this field". The line underneath that field should go red.
* Fill in the field with the following information and the line underneath that field should go green, <b>CLICK "Add To Inventory"</b>:
    * LE200
* You should get a prompt just below the Quantity field that says "Please fill in this field". The line underneath that field should go red.
* Fill in the field with the following information and the line underneath that field should go green, <b>CLICK "Add To Inventory"</b>:
    * 2
* The page will refresh and the form will refresh and appear blank, a flash message will appear across the top of the page with "Inventory Successfully Added". That inventory entry will have been uploaded to the MongoDB database. The form is now ready to be filled out again should a user want to upload more than one inventory entry to the database.

### Edit Inventory
* Load the Website. 
* Right click and select inspection.
* Follow the Log In steps to log into JackSoundSystem profile. 
* Using either the navigation bar or remote view navigation bar <b>CLICK "My Inventory"</b>. You should be transported to the "My Inventory" page.
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy form and all of its attributes are appearing as designed.
* When you arrive at the "My Inventory" page you will see a title that says "My Inventory" and below that will be a card with the inventory entry you just created when you tested the "Add Inventory" function.
* <b>CLICK "Edit"</b> call to action button and a page almost identical to the "Add Inventory" will appear, prefilled with the inventory entry from the card your attempting to edit. 
* Delete "LE200" from the Product name field and replace with "LE400", then <b>CLICK "Cancel"</b>.
* You should be transported back to the "My Inventory" page and the product name hasn't been changed to "LE400", it remains "LE200". This proves the cancel edit inventory function works as designed.
* <b>CLICK "Edit"</b> call to action button and a page almost identical to the "Add Inventory" will appear, prefilled with the inventory entry from the card your attempting to edit. 
* Delete "LE200" from the Product name field and <b>CLICK "Confirm Edit"</b>, you should get a prompt saying "Please fill in this field". 
* Repeat previous instruction with all fields of the form to confirm validators are functioning as designed. 
* Refill all of the fields with orginal information and <b>CLICK "Confirm Edit"</b>, as a reminder I have included the information below: 
    * Category drop down select - Monitors
    * Brand Name - Martin Audio 
    * Product Name - LE200
    * Quanity 2
* Delete "LE200" from the Product name field and replace with "LE400" and<b>CLICK "Confirm Edit"</b>.
* You should be transported back to the "My Inventory" page and the edits you have just made should have been uploaded to the MongoDB database, and be rendered in the card on the page. 

### Delete Inventory
* Load the Website. 
* Right click and select inspection.
* Follow the Log In steps to log into JackSoundSystem profile. 
* Using either the navigation bar or remote view navigation bar <b>CLICK "My Inventory"</b>. You should be transported to the "My Inventory" page.
* Change screen size from desktop to tablet, then change from tablet to smaller devices and verfiy form and all of its attributes are appearing as designed.
* When you arrive at the "My Inventory" page you will see a title that says "My Inventory" and below that will be a card with the inventory entry you created when you tested the "Add Inventory" function.
* <b>CLICK "Delete"</b>.
* A Modal should appear with a title saying "Warning" and just below that a subtitle saying "Are you sure you want to delete this inventory". Below that two call to action buttons titled "No" and "Yes". 
* <b>CLICK "No"</b>.
* You will be transported back to the "My Inventory" page. 
* <b>CLICK "Delete"</b>.
* The same Modal will appear, this time <b>CLICK "Yes"</b>. 
* YOu will be transported back to the "My Inventory" page, and the card with the inventory entry you created will have disappeared. This confirms that the delete function is working as designed. 

### Search Function
* Load the Website. 
* Right click and select inspection.
* At this point you could either follow the Log In steps to log into JackSoundSystem profile, go straight onto the following steps. The search function will work on both sides of the website "Visitor Side" and "Members Side". 
* Using either the navigation bar or remote view navigation bar <b>CLICK "Search Inventory"</b>. You should be transported to the "Search Inventory" page.
* Once there you should see a main title saying "Search Inventory", just below that a form with a text input with a label saying "Search Inventories", and two call for action buttons one labelled "Rest" and the other "Search". 
* For this test I have creatd a number of profiles following the "Register" testing steps mentioned prevously in this testing document. I've also added inventory entries to those profiles using the "Add Inventory" testing steps mentioned prevously in this testing document. 
* Perform the following manual check <b>TYPE "Midas" in Text Input > CLICK "Search" Button</b>. 
* Below the search form all of inventory entries that include the word "Midas" should appear in there own individual cards. 
* Each card should have the name of the company, the inventory entry detailing the category, brand name, product name and quantity of that product they have in stock. 
* Below the inventory entry informatiom you should see a collaposible with "Click for COMPANY NAME Contact Detials, <b>CLICK the collapsible</b>.
* Once clicked the collapsible should expand, to unvale said companies contact details, so you can call them to discuss renting said equipment featured on that particular inventory entry. 
* Scrooll up to the top of the page and <b>CLICK "Reset"</b>



