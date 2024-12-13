# About
This is a Flask-based application that functions as an interactive story platform. The story is loosely based on a 'choose your own adventure' story from a Donald Duck comic [1]. The story includes multiple decision points where the user is presented with choices. At each decision point, the user can influence the story using their voice. The application processes these voice inputs and directs the story based on the user's choices.

# Usage instructions
1. Navigate to the top directory of this project (the directory in which this README file is located)
2. Create a virtual environment for Python3 and activate it.
3. Install the dependencies with `pip install -r requirements.txt`
4. Install the language model that SpaCy uses with the command `python3 -m spacy download en_core_web_md`.
5. Run the project with the command `flask run`. 
6. To access the interface, open a web browser and navigate to the URL displayed in the output, e.g., http://localhost:5000.


# References
[1] Diverse scenarists and diverse drawers. Donald Duck - Megapocket: Zomer 2015, volume Zomer 2015 of Donald Duck - Megapocket. Sanoma, June 2015

