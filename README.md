# DreamDog

Project Title: Dream Dog		
By Ashley Gittens, Bibi Alli, Kristina Cayetano, Miguel Zeng

The project that our group has decided to work on is “Dream Dog.”  According to the census, approximately 42.5 million households in the U.S. own one or more dogs and there are over 73 million dogs in the US! There are so many different kinds(/breeds) of dogs that it can become tough and daunting choosing the ‘right kind of’ dog that fits you. Dream dog makes the process alot easier for you.  The goal of “Dream Dog” is to find the perfect dog breed for the user based on the user’s preferences. The user would also get to interact with other users on the site that have their ‘dream’ dog by sending a ‘bark.’ 
One of the steps involved in Project Dream Dog is making a website. The website will consist of five pages: a Home Page, Make a Match, List of Dogs, Game, About Us and Contact.  The Home Page will have a ‘Log In’ feature so the user can come back to their previous dog results and will also contain the site’s introduction. The ‘Make a Match’ page is where the user will give their input on their dog preferences. There will be five input fields: Personality, Housing, Lifestyle, Preferred Dog Choice, and Climate. After filling in all fields, the results would show the dog breed that best fits the user’s needs. Also as part of the results, there will be a listing of people who own the same dog as the one recommended whom you can send a ‘bark’ to if you’d like to meet up. The ‘List of Dogs’ page contains a list of all of the dog breeds in the database along with their information. The ‘Game’ Page is where the user can have fun, relax and play a small game called ‘Dog Dodge’. The ‘About Us’ page will have a description of each project team member and the user will get to learn interesting things about the group members. Finally, the ‘Contact’ page will contain information on how to get in touch with the ‘Dream Dog’ team and you’d also get to express any questions or concerns you may have. 
As mentioned before, the ‘Game’ Page will contain a fun arcade game called ‘Dog Dodge’. The game ‘Dog Dodge’ is based on the event that commonly occurs in households in which people usually would accidently or purposely throw food under the table for their dog. In the game, the dog would have to catch the food and avoid any knives or plates. The user will possibly get a chance to move through different levels of the game and their score will be tracked. If they get hit too many times, then it would be game over. The game is created in Unity3d with C sharp scripts.
In order to reach the goals of ‘Dream Dog’, data will have to be found and analyzed. The ‘Database of Dogs from the American Kennel Club’ contains the information on all the dog breeds which would also be used for the ‘List of Dogs’ page. The user input data will be used to find the dog breed. The Login/Account data will be used to remember previous user info, accounts. The results records data will need to be stored for previous users along with log statistics for server crashes and general statistics. These are the databases that will need to be implemented.
The Algorithm will use the data collected from American Kernel and compare it with the user’s input preferences. We will implement an AVL Tree (height balanced bst) with public operations such as void insert( x ) which inserts x, void remove( x ) which removes x, bool contains( x )  which returns true if x is present, bool isEmpty( ) which returns true if empty and else false, void makeEmpty( ) which removes all items, void printTree( ) which prints tree in sorted order, Comparable getElement( ) which returns element of a node, int getTotalNodes( ) which returns total number of nodes, int getHeight( ) which returns height of the tree, and Comparable findMaxMatch() which return max Comparable element. Then create a parser to read the database and construct the the tree accordingly.

The tree will store a class object named DogBreed containing private data members:

string breed; //name of the dog breed
string personality;
size_t personality_rate;
string lifestyle;
		 size_t lifestyle_rate;
string housing;
		 size_t housing_rate;
string climate;
		 size_t climate_rate;
string size;
		 size_t size_rate;
size_t match = 0; //match up to 100%

The logic behind this is that each dog breed will be assigned tags and a corresponding rate upon insertion to the tree. For example,

n.breed = "siberian husky"
n.personality = "friendly";
	        n.personality_rate = 17; //out of 20
n.lifestyle = "active";
	        n.lifestyle_rate = 20;
n.housing = "patio";
	        n.housing_rate = 12;
n.climate = "winter";
	        n.climate_rate = 17;
n.size = "large";
	        n.size_rate = 13;
	n.match = 0 //initialized at 0

Each tag’s corresponding rate will be added to the size_t match only if the user has chosen the corresponding tag. For example,
if (user_choice_personality == "friendly") {
		n.match += n.personality_rate;
}
 … //do the same for other tags
 if (user_choice_size == "large") {
		n.match += n.size_rate;
}
Finally, once the user has finished the survey/game, Comparable findMaxMatch( ) is called to find and return the dog breed/s with the highest match value.

The tools that will be used to implement for this project will be Python for the data (database option still to be determined), C++ for AI, C# for the game (Unity?), and PHP/ HTML for the website and data, hosted on a Github. Each team member will be focusing on different aspects of the project while also collaborating on some parts. Bibi Alli will work on the website. Ashley Gittens will work on the game. Kristina Cayetano will work on the algorithm. Miguel Zeng will work on the database. Although there are distinct parts we each need to focus on, we agreed as a team to help one another. Kristina will be helping Bibi with the website’s graphics. Ashley will be helping Kristina with the AI, and Miguel will supervise the team and ensure deadlines are met.
There are also a few other things that have to be decided on like the dream dog logo as well as designs.  Also the dataset and webpages are subject to change as new ideas are formed throughout the progress of the project. 

