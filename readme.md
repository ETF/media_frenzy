Media Frenzy Project
===
Created and agreed to by ETF, teddymcw, asciimo on 2014-01-11.

Purpose
---
Media Frenzy is designed to present a comparison of the main stream media's portrayal of an event with Media Frenzy users' perception of an event. Using key word frequency analysis and real-time visualizations, Media Frenzy will provide a snapshot of the perception-variance between user perception and media depictions. 

Media Frenzy will use public news sources to gather keywords related to an event or article, generate a plaintext version of the content for Media Frenzy user viewing, and create visualizations based on keyword frequency analysis of the news content.

Media Frenzy will allow users to comment on articles and events, read a plaintext version of the content, and allow user comments to generate visualizations based on keyword frequency analysis.

User Interface Structure
---
The Media Frenzy site will consist of two main sections:
 - Landing page/Directory Page
 - Interaction Page

### Directory page will consist of:
 - "Register or Log In" controls in upper-right-hand corner 
 - A collection of buttons representing trending topics
 - A copy of the user-generated visualization being displayed on the interaction page with the most number of user comments (the "hot event" or "event of the moment")
 - Functionality to create new frenzies
 - A bitcoin widget (Coinbase or BitPay) for donations
 - A contact button or forum to email the founders
   - Possibly use Flask Mail extension
 - Privacy, Legal, About, Jobs, etc.
 - The total number of "Interaction Page" instances

### Interaction pages will consist of:
 - Three sections/panels:
   - Media sentiment panel and article list (25%)
     - Top: sentiment bubbles
     - Bottom: Article sources and links, and tiny form to submit more article sources (See new artcile processing section.)
   - Plaintext content (50%)
     - 100% article content
   - User sentiment panel and comments  (25%)
     - Top: sentiment bubbles
     - Bottom: User comments

#### Media Sentiment Panel will consist of:
 - A title section indicating it is the media sentiment portion of the "Interaction Page"
 - Visualizations depicting the most frequently used words with media articles
 - Certain stopwords will be excluded such as: the, an, a, etc.
 - A list of links to source media related to the topic, ranked by the first source used to generate the interaction page
    - Icon for additional metadata modal including: submitted by, date submitted, source, etc.
 - Functionality: When a link is clicked on, the plaintext of the content will be displayed in the "Plaintext version of content" section
 - After a newly submitted article is processed, it will appear in the media sentiment article list, and the sentiment visualization will update accordingly.

#### Plaintext content will consist of:
 - A title section indicating it is the article content portion
 - The title of the content
 - Plaintext version of the content
 - Scroll bar to scroll through content

#### User comment section will consist of:
 - A title section indicating it is the user sentiment portion
 - Visualization of the user comments based on keyword frequency analysis
 - Keyword frequency analysis should be performed each time a new comment is added
 - Visualization should change as keyword frequency analysis changes
 - User generated comments
   - The ability for users to reply to other users
   - Scroll bar to scroll through comments
 - Functionality: Each comment will be parsed to remove exclusion words (the, an, a, etc) and then added to a table for each of the words used
 - If a user is not signed in, the comment area will contain the "Register or Log In to Comment" controls

### Global Elements
 - User log in status in upper-right-hand  corner of every page.  Eg. a username on an expandable tab that, when clicked, reveals controls for user profile settings.

### Backend Functionality
 - New artcile processing (fetching, storing, word frequency analysis, metadata storing)

The project will be considered complete when:
---
1. The two page types exists and are functioning properly
1. New "Interaction Pages" can be generated
1. The visualizations are being populated by keyword frequency analysis for media and user panels
1. Registration and login module is working correctly and secure from malicious foes
1. A copy of the plaintext of content is placed into the "Plaintext content" section
1. Users can comments on articles
1. Users can add new article source links
1. Newly submitted articles update the directory page, as well as the word frequency analysis.

Division of Labor
---
### ETF
#### General Goals
 - Get hands into everything for comprehensive understanding of entire development process.
 - Be able to completely reproduce similar project independently.
 - Understand Flask
 - Understand SQLAlchemy

#### Specific Ownership
 - Project Manage this project.
 - Visualization functionality (D3?)
 - Wireframes and Architecure

### asciimo
#### General Goals
 - Learn the Foundation framework
 - Understand MVC patterns in Flask
 - Better understand advance Python patterns (modules, Object Oriented design)

#### Specific Ownership
 - Content fetching and scraping (Beautiful Soup)
 - NLTK and word frequency process
 - PostreSQL and SQLAlchemy 
 - Git and release management

### teddymcw
#### General Goals
 - Group project flow
 - Solidifying full stack technology (Flask, Foundation, D3) skillz
 - Building something uinque and usable
 - Learn D3

#### Specific Ownership
 - Front-end (Foundation, jinja2, jQuery, Javascript)
 - Flask 

