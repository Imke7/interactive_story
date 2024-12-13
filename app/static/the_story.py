story = {
    "start": {
        "text": 
"""In a small harbor town, two sailors named Moby and Diederik were busy baking a cake for their dog, Goldie, because it was his birthday! They mixed flour, sugar, and eggs, giggling as they decorated the cake with colorful icing and sprinkles.
"Goldie is going to love this!" Moby said, looking happy at their creation.
Once the cake was ready, they rushed to the deck of their boat, but Goldie was nowhere to be found.
"Doesn't Goldie know it's his birthday?" Diederik wondered.
"I don't think dogs understand birthdays," Moby replied. "Let's go find him! He might be at the Black Pearl or down by the pier. Where do you want to look?" """,
        "choices": {
            "Black Pearl": "lvl16",
            "Pier": "lvl19"
        },
        "ending_line": {
            "Black Pearl": "Okay, let's go to the Black Pearl!",
            "Pier": "Okay, let's go to the Pier!"
        }
    },
    # Start over
    "lvl2": {
        "text": 
"""Back on the boat, Moby and Diederik start over.
"Where could Goldie be?" Moby wonders. "Should we check the Black Pearl or the Pier?" """,
        "choices": {
            "Black Pearl": "lvl16",
            "Pier": "lvl19"
        },
        "ending_line": {
            "Black Pearl": "Okay, let's go to the Black Pearl!",
            "Pier": "Okay, let's go to the Pier!"
        }
    },
    # Inspect the warehouse
    "lvl3": {
        "text": 
"""Moby and Diederik ask the warehouse men if they can take a look inside. The men respond immediately, "No way. Curious folks aren't allowed in here. Without written permission from the boss, Magnus, not even the mayor can come in!"
Moby whispers to Diederik, "Magnus is one of the most sneaky and tricky people in town."
The two leave and let the men keep working, but they start to think about how they could still get inside the warehouse. Only two ideas come to mind: they could either pretend to have Magnus's signature, or they could go and ask Magnus himself.""",
        "choices": {
            "Ask Magnus": "lvl9",
            "Forge signature": "lvl23",
        },
        "ending_line": {
            "Ask Magnus": "Good idea! We should just ask him.",
            "Forge signature": "Good idea! Let's try to force his signature.",
        }
    },
    #Huberts Shipyard
    "lvl4": {
        "text": 
"""Diederik and Moby walk into Hubert's workshop. Hubert is busy painting a boat. Moby sees him and says, "The delivery of the boat is late again, huh?"
Hubert laughs. "Yes, just like usual,"  he replies. "I'm a perfectionist. As long as the ship isn't completely finished, I'll keep working on it."
"Quality is important," Diederik agrees, running his hand along the side of the ship and leaving a streak. "It looks great to me," he adds.
Hubert notices the streak and starts to turn red with anger. Diederik whispers to Moby, "Let's get out of here quickly. I don't see Goldie around." 
Moby watches as Hubert's face gets angrier, and they hurry to make their escape.""",
        "choices": {
            ".": "lvl18"
        }
    },
    # Interogate Binky
    "lvl5": {
        "text": 
""""No, Diederik, let's talk to Binky about that cage over by the trash!" says Moby.
"Oh, so you noticed it" says Binky. "When the boss saw Goldie in the warehouse, he decided to trap him to keep him away from the harbor."
"But why?" Diederik asks.
"Because he doesn't like greedy eaters!" says Moby with a grin.
Binky goes on, "He ordered the pirates to take Goldie far away. But then, only the cage came back by mail. I think Goldie escaped!"
"Which pirates were it?" asks Moby. "The Grizzly Gang or Captain Brock's crew?"
Binky starts crying. "I don't knoooow! The boss never tells me anything. He likes Wang better!"
What do you want to do? Look for the Grizzly Gang, find Captain Brock, or ask Wang if he knows anything?""",
        "choices": {
            "Grizzly Gang": "lvl24",
            "Kaptain Brock": "lvl14",
            "Wang": "lvl25"
        },
        "ending_line": {
            "Grizzly Gang": "Alright, let's look for the Grizzly Gang.",
            "Kaptain Brock": "Alright, let's find Captain Brock.",
            "Wang": "Alright, let's ask Wang if he knows anything."
        }
    },
    # climb the hideout of the Grizzly Gang
    "lvl6": {
        "text": 
"""Moby and Diederik climbed to the Grizzly Gang's hideout, but the pirates quickly surrounded them.
"You're caught!" shouted the gang leader. "Surrender now or stay here without food or water!"
"Oh no, we've lost," Moby sighed. "You can take our ship..."
"No need," the leader sneered. "We already have enough treasure!"
Reluctantly, Moby and Diederik handed over their valuables and hurried back down the hill. "What a day," Diederik grumbled. "Let's get back to the bay." """,
        "choices": {
            ".": "lvl18"
        }
    },
    # Continue searching in the Harbour
    "lvl7": {
        "text": 
"""Moby and Diederik continue searching for Goldie in the harbor. They both shout loudly, "Goldieee, where are you?!" 
Goldie should surely come out with all that yelling.
Suddenly, a cat jumps out from a pile of boxes onto Moby! Moby is startled. "The cat was probably mad that we woke him up with all that noise," he says. Moby gently places the cat back onto the boxes where it jumped from.
Moby and Diederik figure that Goldie isn't here; otherwise, he would have heard them shouting.""",
        "choices": {
            ".": "lvl18"
        }
    },
    # Eat food at the Black Pearl
    "lvl8": {
        "text": 
""""You think better on a full stomach," says Diederik, as Nina gestures for the boys to sit down. While Nina goes to get some food, Diederik and Moby suddenly hear a shout: "MOBY! DIEDERIK! COME QUICK!"
They race to the kitchen, hoping to find Goldie. But Nina is holding up a dog toy. "This was just found between two sacks delivered by my errand boy, Wang!"
Diederik sniffs the toy and immediately knows it must belong to Goldie.
"Wang has a shop nearby," Nina explains, "but he also has a warehouse. Where will you go? To the shop or the warehouse?" """,
        "choices": {
            "shop": "lvl25",
            "warehouse": "lvl21"
        },
        "ending_line": {
            "shop": "The shop is a good idea!",
            "warehouse": "The warehouse is a good idea!"
        }
    },
     # At Victor
    "lvl9": {
        "text": 
"""Victor lives in a big villa on a cliff. The house, with its huge roof and tall trees, is already impressive to see. Moby and Diederik have just asked Victor for permission to inspect the warehouse.
Victor starts to laugh, "Ha ha! Why would I help you at all?"
"Because it's Goldie's birthday!" Moby replies.
"Wrong answer," Victor responds. "That dog has already celebrated enough by eating a lot of my supplies."
Suddenly, Binky runs in, saying, "Boss, the pirate Brock is claiming a... a... kidnapping!" Binky didn't see that Victor had guests, or he wouldn't have shared such news.
Victor gets angry with Binky, "DO ME A FAVOR AND SHUT UP, BINKY!"
What do you think? Did Captain Brock kidnap Goldie, or are you going to question Binky outside the villa?""",
        "choices": {
            "Captain Brock Kidnap": "lvl14",
            "Question Binky Outside Villa": "lvl28"
        },
        "ending_line": {
            "Captain Brock Kidnap": "Yes, it's certainly possible that Captain Brock kidnapped Goldie!",
            "Question Binky Outside Villa": "Okay, let's question Binky outside the villa."
        }
    },
     # Wait for the mayors boat to arrive
    "lvl10": {
        "text" : 
"""Diederik and Moby wait for the mayor to arrive. He usually docks at Dock 13, but lately, he's had a lot of accidents there. The mayor finally arrives and walks over the pier. Suddenly, the pier collapses, and the mayor drops all the fish he caught. A whole pack of dogs rushes onto the pier and gobble up all the fish!
"I always have bad luck!" the mayor cries. "I thought it was a Dock 13 but that was not the case." 
After Diederik and Moby have helped the mayor back up to his feet, Diederik says, "I didn't see Goldie among the dogs, so I think he is not here, we should continue looking elsewhere." """,
        "choices": {
            ".": "lvl18"
        }
    },
        # Ask about the Cariage
    "lvl11": {
        "text" : 
""""Does Wang have a carriage?" asks Moby. "That's not an easy thing to own."
"What does Wang have to do with it?" one of the workers says. "Wang only rents the warehouse. The warehouse belongs to Victor."
"Oh, so you're...,” starts Diederik.
"Yes, exactly," the worker replies. "We're Victor's tough crew! Even when we're not at sea, we're working hard here!”
"So where did Goldie go when the boss showed up?" asks Moby.
"We saw Binky chasing him, trying to catch him," says the worker. "But only he and Victor know if he managed to do it."
"Thanks, guys!" says Moby. "Let's go."
Do you want to look for Victor or find Binky?""",
        "choices": {
            "Victor": "lvl9",
            "Binky": "lvl29"
        },
        "ending_line": {
            "Victor": "Okay, we're going to look for Victor.",
            "Binky": "Okay, we're going to find Binky."
        }
    },
    # Run to the hideout of the Grizzly Gang
    "lvl12": {
        "text" : 
""""Raise the sails, Diederik! If they board us, we'll have to say goodbye to our ship!" Moby calls out.
Moby and Diederik hurry to the hideout of the Grizzly Gang. They dock their boat.
"Hurry up!" Moby shouts to Diederik. They race up to the Grizzly Gang's hideout: an old caravan sitting on a tall hill.
Diederik sees that the Grizzly Gang also made land, however Moby sais that it doesn't matter because they are already there.
At the bottom of the hill, the Grizzly Gang is plotting how to catch Moby and Diederik. It seems like they're waiting to see what Moby and Diederik will do next.
What do you want to do? Will you enter the hideout or climb on the roof of the hideout?""",
        "choices": {
            "Enter Hideout": "lvl17",
            "Climb Roof ": "lvl6"
        },
        "ending_line": {
            "Enter Hideout": "Entering the hideout seems like a good choice.",
            "Climb Roof ": "Climbing the hideout seems like a good choice."
        }
    },
    # Talk to Cato and Storm
    "lvl13": {
        "text": 
"""Once the Grizzly Gang and Captain Brock have left, the boys sail further. Cato and Admiral Storm explain what happened to them and how they were captured by Captain Brock.
"The captain got so fed up with all the wild stories Admiral Storm was telling that he decided to dump us off at the first boat he saw," Cato says.
"Have you seen Goldie anywhere?" Moby asks hopefully.
"Unfortunately, no," Cato and Admiral Storm reply.
Disappointed, Moby and Diederik decide that they should go back to the town. The boys drop off Cato and Admiral Storm at the harbor and continue their journey.""",
        "choices": {
            "eat": "."
        }
    },
    # Search for captain Brock
    "lvl14": {
        "text": 
"""Moby and Diederik have taken their boat out of the harbor and are heading out to sea in search of the pirate Captain Brock.
"How are we going to find Captain Brock?" Diederik asks. "We don't even know if he operates in this area."
Moby replies, "We'll stay on the trade route; it's the best area for a pirate looking for..."
Diederik suddenly coughs and spots a ship through his binoculars that's sailing straight toward them. "What should we do, Moby?" he asks.
"Absolutely nothing," Moby says. "If we want answers, we need to let them board us!" """,
        "choices": {
            ".": "lvl22"
        }
    },
    #Outside the black pearl
    "lvl15": {
        "text": 
"""Moby and Diederik stand outside the Black Pearl. Moby asks Diederik if the cake will stay good for a while and whether they're really in a hurry to find Goldie.
Diederik replies, "Yes, the cake should be fine, but I don't think I can resist the temptation to eat it! I love sweets. Why don't we just forget about Goldie and enjoy the cake ourselves?"
Moby grabs Diederik by the arm and pulls him away. "Hold back your taste buds; the search for Goldie must continue! Should we head to the Harbor or go back to Hubert's shipyard?" """,
        "choices": {
            "Harbor": "lvl19",
            "Huberts shipyard": "lvl4",
        },
        "ending_line": {
            "Harbor": "Yes, we should definitely head to the Harbor.",
            "Huberts shipyard": "Yes, we should definitely head to the shipyard.",
        }
    },
    # Go to the Black Pearl
    "lvl16": {
        "text": 
"""Nina's inn is always packed. Surely someone here has news about our friend! 
"Sorry to interrupt your meal, friends," Moby calles out. "We're looking for Goldie! Has anyone seen him today?" 
A man at the bar speaks up. "Have you tried the Harbor? He's usually there, begging for food from the fishing boats." 
At the same time, Nina, the owner of the inn says, "Would you like me to read my fortune cards?"
What would you like to do? Go to the Harbor or let Nina read the fortune cards?""",
        "choices": {
            "Cards": "lvl27",
            "Harbor": "lvl19"
        },
        "ending_line": {
            "Cards": "Yes, maybe the cards can tell us something useful!",
            "Harbor": "Yes, maybe Goldie is at the harbor!"
        }
    },
    # Get onto the roof
    "lvl17": {
        "text": 
"""Diederik grabs the ladder, and Moby kicks in the door of the hideout.
Diederik is confused."'I thought we were going inside?"
"No, we're going on the roof, but we can't go empty-handed," Moby replies. "We need something to keep them at bay." He pauses for a moment and then his face lights up. "I know it! A collector's book! Everyone collects something, and pirates are no exception."
Moby and Diederik climb onto the roof. Just then, the pirates arrive at their hideout. Moby holds their collector's book high in the air.
"Oh no!" cries the Grizzly Gang. "Not our book with all our wanted posters!"
"You'll get it back once you tell us where Goldie is!" shouts Diederik. He hopes that this is going to work.
The leader of the Grizzly Gang sighs. "Okay, fine. He escaped despite the cage; he ran back to the mainland. We think he's haunting us now. We even saw his silhouette in the light of the lighthouse."
Where do you want do look? At Victor, at Wangs shop, the harbor, outside the Black Pearl or at the lighthouse?""",
        "choices": {
            "Victor": "lvl9",
            "Wangs shop": "lvl25",
            "The Harbor": "lvl19",
            "Outside the Black Pearl": "lvl15",
            "Lighthouse": "lvl30"
        },
        "ending_line": {
            "Victor": "Good choice! Let's go to Victor.",
            "Wangs shop": "Good choice! Let's go to Wangs shop.",
            "The Harbor": "Good choice! Let's go to the Harbor.",
            "Outside the Black Pearl": "Good choice! Let's go look outside the Black Pearl.",
            "Lighthouse": "Good choice! Let's go to the lighthouse."
        }
    },
    # Start over
    "lvl18": {
        "text": 
""""Two options are left," says Moby. "We can keep walking in circles, or we can go back to the boat and start over."
Diederik takes and moment to think and then replies, "Let's go back to the boat and try again. But we need to be careful to make different choices this time!" """,
        "choices": {
            ".": "lvl2"
        }
    },
    # Search the Harbour
    "lvl19": {
        "text": 
""""So, where does Goldie usually hide?" Moby wonders. 
"He's usually at Dock 12B," says Diederik and they start to make their way to Dock 12B. When they arrive, Moby and Diederik run into Bert the Boatman. 
"Have you seen our favorite dog, Goldie?" they say in unison.
"Not yet, but he usually shows up when the fishing boat docks," Bert replies.
Moby looks around and he sees that far away, a boat is taking course to the harbor. He squints his eyes. "Whose boat is that coming in?" he asks.
"That boat belongs to the mayor," Bert answers. "Do you want to wait for him to arrive, or do you want to keep looking?" """,
        "choices": {
            "Wait for him to arrive": "lvl10",
            "Continue keep looking": "lvl7"
        },
        "ending_line": {
            "Wait for him to arrive": "Okay, we're going to wait.",
            "Continue keep looking": "Okay, we'll keep looking."
        }
    },
    # Lure Binky the bushes in
    "lvl20": {
        "text": 
"""Diederik takes out a stack of bills from his pocket and waves it above the bushes. Binky's eyes go wide. "Wow! I've never seen that much money in one place!" he says, running over to the bushes.
Moby steps out and says, "Oh? Doesn't Victor pay you well enough?"
Binky gulps. "Moby..."
Diederik steps out too, smiling. "And I'm here as well!"
Binky laughs nervously, "Haha, well, now I feel better!"
Diederik frowns a bit. "You don't think much of me, do you? Let's go, Moby. I've got a feeling this guy has nothing useful to tell us."
Do you take Diederiks advice and leave, or listen to Binky's stories?""",
        "choices": {
            "Diederik Leave": "lvl9",
            "Listen Stories Binky": "lvl5"
        },
        "ending_line": {
            "Diederik Leave": "Good choice! Diederik knows best.",
            "Listen Stories Binky": "Alright, let's give Binky another chance."
        }
    },
    #Warehouse Wang
    "lvl21": {
        "text": 
"""Diederik says to Moby, "I still think we should go to the shop."
"Pointless," replies Moby. "Wang's shop only has the most valuable items. Everything else, even tea, is in this warehouse. So, this must be where Goldie lost his toy."
A bit further along, they see two shady-looking men carrying sacks toward the warehouse. Moby calls out, "Hey guys, working hard?"
One of the men replies sarcastically and a bit annoyed, "No, we're just taking these sacks for a walk or something."
The other man steps forward angrily toward Moby and Diederik, saying, "What do you want here?"
Do you ask to inspect the warehouse, or do you start asking about Goldie?""",
        "choices": {
            "Inspect warehouse": "lvl3",
            "Ask about Goldie": "lvl26"
        },
        "ending_line": {
            "Inspect warehouse": "Asking to inpect the warehouse seems like a good idea.",
            "Ask about Goldie": "Asking about Goldie seems like a good idea."
        }
    },
    # Boarded by the grizzly gang
    "lvl22": {
        "text": 
"""Diederik and Moby let their ship be boarded. In suspense, they wait to see who is coming aboard. Captain Brock and the Grizzly Gang come down the gangplank.
"Huh, I didn't know Captain Brock and the Grizzly Gang were allies," Moby says.
"I have two prisoners for you." Captain Brock announces. "Take them and get them as far away from here as possible!"
Cato and Admiral Storm, good friends of Moby and Diederik, walk off the gangplank! Captain Brock and the Grizzly Gang leave, leaving Diederik and Moby behind with Cato and Admiral Storm.""",
        "choices": {
            ".": "lvl13"
        }
    },
    # Forge signature of Victor
    "lvl23": {
        "text": 
"""Moby and Diederik have forged the signature of the notorious Victor. Luckily, Nina had an old letter that helped the boys copy Victor's handwriting. Cheerfully, Moby and Diederik return to the warehouse men.
"Your boss was very nice! Here is the permission!" Moby shouts as they arrive.
The warehouse men take the letter. "Hmmm, very nice. This is not how we know our boss," one of them says. "This is a forgery; I can see it right away!"
Diederik's heart skips a beat. He really thought this would work. "That can't be! It's his handwriting, and it's signed by ‘Victor’ at the bottom!"
"Exactly," the man replies, "but for his workers, he always signs with ‘The Boss.’"            
"Oh no, this is a mess," Diederik says. "Let's get out of here quickly! Should we search in the harbor or at Hubert's shipyard?" """,
        "choices": {
            "Search the harbor": "lvl7",
            "Huberts shipyard": "lvl4"
        },
        "ending_line": {
            "Search the harbor": "Alright, let's search the Harbor.",
            "Huberts shipyard": "Alright, let's search at the shipyard."
        }

    },
    # Get to the hideout of the Grizzly Gang
    "lvl24": {
        "text": 
"""Moby and Diederik take their boat, The Pearl, out to sea to find the Grizzly Gang.
"Ugh! Waste of time and money!" grumbles Diederik. "What valuable thing did Binky really tell us?"
"Well, he told us the hideout of the Grizzly Gang—don't you think that's worth something?" Moby replies.
"Yeah, if those are the pirates Victor handed Goldie over to, then it is. But are you sure?"
"Absolutely," says Moby. "Victor and Captain Brock aren't friends. So, we need to find the Grizzly Gang."
Just then, Diederik spots a pirate ship sailing straight toward them. "Uh-oh... maybe they're finding us first?",
Should we let the dangerous pirates board us, or should we try to get away?""",
        "choices": {
            "Let pirates board": "lvl22",
            "Get away": "lvl12"
        },
        "ending_line": {
            "Let pirates board": "Letting the pirates board is a brave choice! Let's try it.",
            "Get away": "Yes, we should definitely get away."
        }

    },
    #Shop of Wang
    "lv25": {
        "text": 
"""Diederik and Moby walk into Wang's shop. It's filled with all sorts of unusual items; Wang is a special seller and has everything you can imagine for the right price.
"Hello, friends!" Wang greets them with a smile.
"Wang, have you seen a dog?" asks Moby. 
Wang grabs a large, thick book and starts flipping through the pages. "Let me see how much a dog costs," he says.
"NO! We're not looking for just any dog; we're looking for Goldie!” Diederik exclaims.
Wang replies that he has no idea where Goldie is. Diederik and Moby don't fully trust Wang, but they think he might be telling the truth this time. Knowing Wang, he would have asked for money otherwise.
"What bad luck!" sighs Diederik. "What should we do now? Head to the Harbor, go to the Huberts shipyard, or check outside the Black Pearl?" """,
        "choices": {
            "Harbor": "lvl19",
            "Huberts shipyard": "lvl4",
            "Outside the Black Pearl": "lvl15"
        },
        "ending_line": {
            "Harbor": "Yes, let's head to the Harbor.",
            "Huberts shipyard": "Yes, let's head to Huberts Shipyard.",
            "Outside the Black Pearl": "Yes, let's head to the Black Pearl."
        }
    },
    # Ask about Goldie
    "lvl26": {
        "text": 
""""We're looking for Goldie, a dog who loves to-" 
Moby can't even finish his sentence when the warehouse worker interjects, "EAT! Oh, we know that dog all too well," he says with a groan. "Last night, while we were loading supplies, that dog was sleeping right in the middle of the sacks. That beast drives us mad! We tossed a bag of food at him, trying to shoo him away, and he got so upset that he showed us just how he felt about being woken up. If the boss's carriage hadn't arrived right then, I don't think I'd have a hand left unbitten."
That carriage sounds interesting, but so does the warehouse. What do you want to do? Ask about the carriage or look around the warehouse?""",
        "choices": {
            "Carriage": "lvl11",
            "Inspect Warehouse": "lvl3"
        },
        "ending_line": {
            "Carriage": "The carriage sounds like a promising lead.",
            "Inspect Warehouse": "Okay, let's look around the warehouse."
        }
    },
    # Read Nina's cards
    "lvl27": {
        "text": 
""""It's not the first time Nina's cards have correctly predicted the future," says Moby. 
Nina flips over a card and says, "The one you're looking for would rather be somewhere else."
Diederik sighs, "Here we go again... somewhere else, but where?"
Nina fans out the cards and holds them close to Diederik. "Diederik, pick one while thinking of Goldie," she says.
"Alright," Diederik replies, "but I want a 'chatter card', one that will tell me everything, loud and clear." Diederik picks the two of spades and sighs. "That means we have to figure it out ourselves."
"I am hungry, maybe we should eat first," says Moby, "or do you want to keep searching?" """,
        "choices": {
            "eat": "lvl8",
            "keep searching": "lvl15"
        },
        "ending_line": {
            "eat": "You can't think straight on an empty stomach. Eating seems like a good idea.",
            "keep searching": "Goldie is too important! We should indeed keep searching."
        }
    },
    # Question Binky Outside Villa
    "lvl28": {
        "text": 
"""Moby and Diederik confront Binky outside the big house. "What do you want from me?" asks Binky.
"Ohhh, nothing much. Can't we just have a little chat?" says Diederik.
"I'd like to...," Binky says nervously. "but the boss wouldn't be happy about it." With those words, Binky quickly runs back inside and slams the door shut.
"What do we do now?" asks Diederik.
Moby turns to Diederik. "Good question...," he says.
Do you want to go back to the harbor or head into town?""",
        "choices": {
            "Harbor": "lvl7",
            "Town": "lvl15"
        },
        "ending_line": {
            "Harbor": "Alright, let's go back to the harbor. Maybe we're in luck this time.",
            "Town": "Alright, let's head into town."
        }
    },
    # Talk to Binky
    "lvl29": {
        "text" : 
"""Moby and Diederik sneak over to Victor's big house. They hide in the bushes outside, waiting to talk to Binky. "We can't get Victor involved," Moby whispers. "Who knows what excuse he'll make up to trick us."
"WATCH OUT! There he is!" says Moby as Binky steps out the door. Moby whispers from the bushes, "Pssst, Binky!"
Binky looks around, surprised. "Wwwwho's there?" he stammers nervously. "Friend or foe?"
"What should we do?" whispers Diederik. "Should we lead Binky into the woods or reveal ourselves?" """,
        "choices": {
            "Lead into woods": "lvl20",
            "Reveal ourselves": "lvl28"
        },
        "ending_line": {
            "Lead into woods": "Okay, let's try leading him into the woods.",
            "Reveal ourselves": "Okay, let's reveal ourselves."
        }
    },
    # Go to the lighthouse
    "lvl30": {
        "text" : 
""""Why do you think Goldie is here at the lighthouse?" Diederik asks.
"Think about it," Moby replies. "The Grizzly Gang said they felt like Goldie was still following them because they saw his shadow in the lighthouse light. But Diederik, why did you even bring the cake if you don't think Goldie is here?"
"Well, I'll just eat this cake if he's not here and move his birthday to February 30," Diederik says with a mischievous grin.
"But that can't be!" Moby exclaims.
"And that's exactly why I'm doing it," Diederik laughs.
Suddenly, the front door of the lighthouse bursts open, and Reginald O'Connor stands there.
"What an honor to have you visit!" he says warmly.
"We're looking for Goldie," Moby says.
"You're in luck! She—" Just then, something rushes past them, and the whole cake is gone in an instant!
"HE'S HERE!" Moby and Diederik shout in unison.""",
        "choices": {
            ".": "lvl31",
        }
    },
    # Finish
    "lvl31": {
        "text": 
""""Reginald O'Connor says, "Goldie is here, but has nothing to do with this. Come, I will show you!"
Reginald O'Connor shows a nest of puppies. "Look, these are Goldie's children: Silvy, Bronzy, Nickly and Tinny."
Moby and Diederik can hardly believe their eyes. What a cute nest of puppies!
"Well, it looks like Goldie is actually a 'she'," Moby says with a smile on his face. 
Then Goldie appears, wagging her tail, as proud as can be of her children. Moby and Diederik give her a big hug.        
"There's just one more thing to do," says Diederik. "SING!"
All around the bay, people can be heard singing: "LONG MAY SHE LIVE, LONG MAY GOLDIE LIVE, IN GLORYAAAA, HIP, HIP HOORAY!"
And that is the end of the story of Moby, Diederik, and Goldie's birthday!""",                               
        "choices": {
            ".": "end",
        }
    },
}