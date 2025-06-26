from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List

router = APIRouter()

class QuizInput(BaseModel):
    answers: Dict[str, str]

class QuizResponse(BaseModel):
    utensil: str
    emoji: str
    description: str
    traits: List[str]
    strengths: List[str]
    compatibility: List[Dict[str, str]]
    personality_insights: List[str]
    fun_facts: List[str]

class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[Dict[str, str]]

@router.get("/questions")
async def get_quiz_questions():
    """Get all quiz questions"""
    return quiz_questions

@router.post("/submit", response_model=QuizResponse)
async def submit_quiz(quiz_input: QuizInput):
    # Calculate utensil personality based on answers
    utensil_result = calculate_utensil_personality(quiz_input.answers)
    return utensil_result

@router.get("/")
async def quiz_response():
    # For now, return a placeholder utensil
    return {
        "utensil": "Spatula",
        "traits": ["Helpful", "Flexible", "Reliable"],
        "summary": "You're the go-to tool when things get sticky!"
    }

# Quiz questions data
quiz_questions = [
    {
        "id": "morning_routine",
        "question": "How do you typically start your morning in the kitchen? ☀️",
        "options": [
            {
                "key": "quick_efficient",
                "text": "Quick and efficient - grab what I need and go!",
                "traits": ["efficient", "practical", "sharp"]
            },
            {
                "key": "slow_methodical",
                "text": "Slow and methodical - I like to prepare everything carefully",
                "traits": ["patient", "thorough", "gentle"]
            },
            {
                "key": "creative_experimental",
                "text": "Creative and experimental - I love trying new breakfast ideas!",
                "traits": ["creative", "versatile", "innovative"]
            },
            {
                "key": "simple_reliable",
                "text": "Simple and reliable - same routine, works every time",
                "traits": ["consistent", "reliable", "steady"]
            }
        ]
    },
    {
        "id": "cooking_style",
        "question": "What's your preferred cooking style? 👨‍🍳",
        "options": [
            {
                "key": "precise_measurements",
                "text": "I measure everything precisely and follow recipes exactly",
                "traits": ["precise", "methodical", "reliable"]
            },
            {
                "key": "intuitive_tasting",
                "text": "I cook by intuition, tasting and adjusting as I go",
                "traits": ["intuitive", "flexible", "sensory"]
            },
            {
                "key": "bold_experimenting",
                "text": "I love experimenting with bold flavors and techniques",
                "traits": ["adventurous", "creative", "bold"]
            },
            {
                "key": "comfort_classics",
                "text": "I stick to comfort food classics that everyone loves",
                "traits": ["nurturing", "traditional", "warm"]
            }
        ]
    },
    {
        "id": "social_cooking",
        "question": "How do you feel about cooking with others? 👥",
        "options": [
            {
                "key": "love_collaboration",
                "text": "I love it! The more hands, the merrier!",
                "traits": ["social", "collaborative", "inclusive"]
            },
            {
                "key": "prefer_solo",
                "text": "I prefer cooking alone - it's my meditation time",
                "traits": ["independent", "focused", "introspective"]
            },
            {
                "key": "enjoy_teaching",
                "text": "I enjoy teaching others and sharing techniques",
                "traits": ["helpful", "patient", "knowledgeable"]
            },
            {
                "key": "situational",
                "text": "It depends on my mood and what I'm making",
                "traits": ["adaptable", "balanced", "flexible"]
            }
        ]
    },
    {
        "id": "kitchen_organization",
        "question": "How do you keep your kitchen organized? 🏠",
        "options": [
            {
                "key": "everything_place",
                "text": "Everything has its place and I keep it there",
                "traits": ["organized", "systematic", "tidy"]
            },
            {
                "key": "functional_chaos",
                "text": "It looks chaotic but I know where everything is",
                "traits": ["creative", "unconventional", "intuitive"]
            },
            {
                "key": "minimalist_essential",
                "text": "I keep only the essentials - less is more",
                "traits": ["minimalist", "practical", "efficient"]
            },
            {
                "key": "constantly_rearranging",
                "text": "I'm constantly rearranging to optimize my workflow",
                "traits": ["perfectionist", "detail-oriented", "improving"]
            }
        ]
    },
    {
        "id": "favorite_meal_prep",
        "question": "What's your favorite type of meal to prepare? 🍽️",
        "options": [
            {
                "key": "elaborate_dinners",
                "text": "Elaborate dinners with multiple courses",
                "traits": ["ambitious", "sophisticated", "thorough"]
            },
            {
                "key": "quick_healthy",
                "text": "Quick, healthy meals that fuel my day",
                "traits": ["practical", "health-conscious", "efficient"]
            },
            {
                "key": "comfort_soul",
                "text": "Comfort food that warms the soul",
                "traits": ["nurturing", "emotional", "caring"]
            },
            {
                "key": "artistic_presentation",
                "text": "Beautiful dishes that are almost too pretty to eat",
                "traits": ["artistic", "detail-oriented", "aesthetic"]
            }
        ]
    },
    {
        "id": "kitchen_challenges",
        "question": "How do you handle kitchen mishaps and mistakes? 😅",
        "options": [
            {
                "key": "learn_adapt",
                "text": "I learn from them and adapt quickly",
                "traits": ["resilient", "learning", "adaptable"]
            },
            {
                "key": "stay_calm",
                "text": "I stay calm and find creative solutions",
                "traits": ["calm", "problem-solving", "creative"]
            },
            {
                "key": "start_over",
                "text": "I prefer to start over and do it right",
                "traits": ["perfectionist", "determined", "thorough"]
            },
            {
                "key": "laugh_it_off",
                "text": "I laugh it off - cooking should be fun!",
                "traits": ["optimistic", "easygoing", "joyful"]
            }
        ]
    },
    {
        "id": "texture_preference",
        "question": "What textures do you gravitate toward in cooking? 🤤",
        "options": [
            {
                "key": "smooth_creamy",
                "text": "Smooth and creamy - like perfect sauces and soups",
                "traits": ["smooth", "gentle", "comforting"]
            },
            {
                "key": "crispy_crunchy",
                "text": "Crispy and crunchy - I love that satisfying bite",
                "traits": ["sharp", "precise", "satisfying"]
            },
            {
                "key": "light_airy",
                "text": "Light and airy - like perfectly whipped cream",
                "traits": ["light", "delicate", "ethereal"]
            },
            {
                "key": "hearty_substantial",
                "text": "Hearty and substantial - food that sticks to your ribs",
                "traits": ["substantial", "grounding", "nourishing"]
            }
        ]
    },
    {
        "id": "entertaining_style",
        "question": "How do you approach entertaining guests? 🎉",
        "options": [
            {
                "key": "elaborate_impressive",
                "text": "I go all out with elaborate, impressive spreads",
                "traits": ["ambitious", "sophisticated", "impressive"]
            },
            {
                "key": "casual_comfortable",
                "text": "I keep it casual and comfortable - the vibe matters most",
                "traits": ["relaxed", "welcoming", "comfortable"]
            },
            {
                "key": "interactive_experience",
                "text": "I love creating interactive cooking experiences",
                "traits": ["engaging", "interactive", "fun"]
            },
            {
                "key": "simple_elegant",
                "text": "I prefer simple but elegant presentations",
                "traits": ["elegant", "minimalist", "refined"]
            }
        ]
    },
    {
        "id": "kitchen_learning",
        "question": "How do you prefer to learn new cooking techniques? 📚",
        "options": [
            {
                "key": "experiment_fail",
                "text": "I learn by experimenting and learning from failures",
                "traits": ["adventurous", "resilient", "learning"]
            },
            {
                "key": "research_plan",
                "text": "I research thoroughly and plan before trying",
                "traits": ["methodical", "prepared", "thorough"]
            },
            {
                "key": "learn_others",
                "text": "I learn best from others and collaborative experiences",
                "traits": ["social", "collaborative", "open-minded"]
            },
            {
                "key": "intuitive_feel",
                "text": "I trust my intuition and natural feel for cooking",
                "traits": ["intuitive", "natural", "instinctive"]
            }
        ]
    },
    {
        "id": "cooking_motivation",
        "question": "What motivates you most in the kitchen? 💝",
        "options": [
            {
                "key": "nourish_loved",
                "text": "Nourishing and caring for the people I love",
                "traits": ["nurturing", "caring", "loving"]
            },
            {
                "key": "creative_expression",
                "text": "Creative expression and artistic satisfaction",
                "traits": ["creative", "artistic", "expressive"]
            },
            {
                "key": "stress_relief",
                "text": "Stress relief and therapeutic relaxation",
                "traits": ["therapeutic", "calming", "mindful"]
            },
            {
                "key": "skill_mastery",
                "text": "Mastering skills and achieving perfection",
                "traits": ["ambitious", "focused", "determined"]
            }
        ]
    }
]

def calculate_utensil_personality(answers: Dict[str, str]) -> QuizResponse:
    """Calculate utensil personality based on quiz answers"""
    
    # Count traits from answers
    trait_counts = {}
    for question_id, answer in answers.items():
        question = next((q for q in quiz_questions if q["id"] == question_id), None)
        if question:
            option = next((opt for opt in question["options"] if opt["key"] == answer), None)
            if option:
                for trait in option["traits"]:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
    
    # Determine utensil based on dominant traits
    utensil_type = determine_utensil(trait_counts)
    
    # Get utensil details
    utensil_details = get_utensil_details(utensil_type)
    
    return QuizResponse(
        utensil=utensil_details["name"],
        emoji=utensil_details["emoji"],
        description=utensil_details["description"],
        traits=utensil_details["traits"],
        strengths=utensil_details["strengths"],
        compatibility=utensil_details["compatibility"],
        personality_insights=utensil_details["personality_insights"],
        fun_facts=utensil_details["fun_facts"]
    )

def determine_utensil(trait_counts: Dict[str, int]) -> str:
    """Determine utensil type based on trait counts"""
    
    # Define utensil criteria
    utensil_criteria = {
        "wooden_spoon": ["nurturing", "comforting", "caring", "gentle"],
        "chef_knife": ["sharp", "precise", "efficient", "determined"],
        "whisk": ["creative", "versatile", "energetic", "social"],
        "cast_iron_pan": ["steady", "consistent", "reliable", "patient"],
        "measuring_cup": ["precise", "methodical", "reliable", "organized"],
        "tongs": ["detail-oriented", "thorough", "patient", "systematic"],
        "spatula": ["flexible", "adaptable", "helpful", "reliable"],
        "grater": ["precise", "gentle", "patient", "thorough"],
        "colander": ["filtering", "organized", "practical", "efficient"],
        "rolling_pin": ["steady", "consistent", "reliable", "patient"],
        "peeler": ["precise", "gentle", "patient", "thorough"]
    }
    
    # Calculate scores for each utensil
    utensil_scores = {}
    for utensil, traits in utensil_criteria.items():
        score = sum(trait_counts.get(trait, 0) for trait in traits)
        utensil_scores[utensil] = score
    
    # Return the utensil with the highest score
    return max(utensil_scores, key=utensil_scores.get)

def get_utensil_details(utensil_type: str) -> Dict:
    """Get detailed information about a utensil"""
    
    utensil_data = {
        "wooden_spoon": {
            "name": "Wooden Spoon",
            "emoji": "🥄",
            "description": "You're the heart and soul of the kitchen! Like a trusty wooden spoon, you're gentle, nurturing, and always there when needed. You bring warmth and comfort to everything you touch, and people naturally turn to you for support and care.",
            "traits": [
                "Nurturing and caring by nature",
                "Gentle but incredibly strong",
                "Traditional values with timeless wisdom",
                "Natural mediator and peacekeeper"
            ],
            "strengths": [
                "You make everyone feel welcomed and loved",
                "Excellent at bringing people together",
                "Patient and understanding listener",
                "Create comfort and stability for others"
            ],
            "compatibility": [
                {"name": "Cast Iron Pan", "emoji": "🍳", "reason": "You both appreciate tradition and get better with time!"},
                {"name": "Measuring Cup", "emoji": "📏", "reason": "Your caring nature pairs perfectly with their precision!"},
                {"name": "Kitchen Tongs", "emoji": "🦞", "reason": "Both of you are always ready to help others!"}
            ],
            "personality_insights": [
                "You have an old soul with timeless wisdom that others seek out.",
                "Your nurturing nature makes you a natural caregiver.",
                "You create spaces where people feel safe and loved."
            ],
            "fun_facts": [
                "You probably give the best hugs and make people feel instantly comfortable",
                "Your friends come to you first when they need advice or comfort",
                "You have a secret talent for making everything feel like home",
                "You're the type who remembers everyone's favorite comfort food"
            ]
        },
        "chef_knife": {
            "name": "Chef's Knife",
            "emoji": "🔪",
            "description": "You're sharp, efficient, and get straight to the point! Like a quality chef's knife, you're precise, reliable, and absolutely essential. You tackle challenges head-on with skill and confidence, and others rely on your expertise.",
            "traits": [
                "Direct and decisive in approach",
                "Highly skilled and competent",
                "Natural leader and problem-solver",
                "Values precision and excellence"
            ],
            "strengths": [
                "You cut through confusion to find solutions",
                "Highly efficient and productive",
                "Others look to you for guidance",
                "Excellent at handling complex situations"
            ],
            "compatibility": [
                {"name": "Cutting Board", "emoji": "🪵", "reason": "You're unstoppable when you have solid support!"},
                {"name": "Sharpening Steel", "emoji": "⚔️", "reason": "They help keep your edge sharp and ready!"},
                {"name": "Measuring Cup", "emoji": "📏", "reason": "Precision meets precision - a perfect match!"}
            ],
            "personality_insights": [
                "You're a natural leader who others turn to when decisions need to be made.",
                "You value efficiency and direct communication.",
                "You have a keen eye for detail and precision."
            ],
            "fun_facts": [
                "You're probably really good at making quick decisions under pressure",
                "People describe you as having a 'sharp wit' and keen insight",
                "You likely have a collection of high-quality tools or items you treasure",
                "You're the friend who can solve problems others find impossible"
            ]
        },
        "whisk": {
            "name": "Whisk",
            "emoji": "🥛",
            "description": "You're the ultimate multitasker and social butterfly! Like a whisk, you're energetic, versatile, and amazing at bringing different elements together. You add lightness and joy to every situation and can handle multiple things at once with grace.",
            "traits": [
                "Energetic and always in motion",
                "Excellent at multitasking",
                "Brings people and ideas together",
                "Optimistic and uplifting presence"
            ],
            "strengths": [
                "You create harmony from chaos",
                "Natural at networking and connecting others",
                "Bring lightness to heavy situations",
                "Incredibly adaptable and flexible"
            ],
            "compatibility": [
                {"name": "Mixing Bowl", "emoji": "🥣", "reason": "You create magic together in perfect harmony!"},
                {"name": "Kitchen Tongs", "emoji": "🦞", "reason": "Both versatile multitaskers who get things done!"},
                {"name": "Wooden Spoon", "emoji": "🥄", "reason": "Your energy complements their steady warmth!"}
            ],
            "personality_insights": [
                "Your positive energy is contagious and lifts up everyone around you.",
                "You love bringing people together and creating connections.",
                "You have a creative spirit that can't be contained."
            ],
            "fun_facts": [
                "You probably love hosting parties and bringing people together",
                "You have an amazing ability to lighten the mood in any situation",
                "You're likely great at juggling multiple projects or hobbies",
                "Your energy level amazes (and sometimes exhausts) your friends"
            ]
        },
        "cast_iron_pan": {
            "name": "Cast Iron Pan",
            "emoji": "🍳",
            "description": "You're solid, dependable, and only get better with time! Like cast iron, you're incredibly durable and versatile. You might take a while to warm up, but once you do, you maintain that warmth beautifully and can handle anything life throws at you.",
            "traits": [
                "Steady and incredibly reliable",
                "Gets better with experience",
                "Can handle high-pressure situations",
                "Traditional and time-tested approach"
            ],
            "strengths": [
                "You provide consistent, reliable results",
                "Extremely versatile and adaptable",
                "Others depend on your stability",
                "You improve and mature with every challenge"
            ],
            "compatibility": [
                {"name": "Wooden Spoon", "emoji": "🥄", "reason": "Classic combination that never goes out of style!"},
                {"name": "Chef's Knife", "emoji": "🔪", "reason": "Both reliable tools that professionals depend on!"},
                {"name": "Heat-Resistant Spatula", "emoji": "🍴", "reason": "They can handle your intensity and heat!"}
            ],
            "personality_insights": [
                "You're the foundation that others build upon - steady and strong.",
                "You get more interesting and valuable with every year that passes.",
                "You're someone people can always depend on in a crisis."
            ],
            "fun_facts": [
                "You get more interesting and valuable with every year that passes",
                "You're probably someone people can always depend on in a crisis",
                "You likely have some skills or hobbies you've been perfecting for years",
                "Your friends know you'll still be there for them decades from now"
            ]
        },
        "measuring_cup": {
            "name": "Measuring Cup",
            "emoji": "📏",
            "description": "You're precise, organized, and love bringing structure to chaos! Like a measuring cup, you're all about accuracy and helping others get the perfect balance. You're the friend people call when they need things done right.",
            "traits": [
                "Detail-oriented and meticulous",
                "Loves organization and structure",
                "Values accuracy and precision",
                "Helpful and reliable guide for others"
            ],
            "strengths": [
                "You help others achieve perfect balance",
                "Excellent at planning and organizing",
                "People trust your judgment and advice",
                "You bring order to chaotic situations"
            ],
            "compatibility": [
                {"name": "Kitchen Scale", "emoji": "⚖️", "reason": "You both value accuracy and perfect measurements!"},
                {"name": "Chef's Knife", "emoji": "🔪", "reason": "Precision tools that create professional results!"},
                {"name": "Recipe Book", "emoji": "📖", "reason": "You both believe in following the right formula!"}
            ],
            "personality_insights": [
                "You bring balance and harmony to chaotic situations.",
                "You're very methodical and precise in your approach.",
                "You believe in following proven methods and recipes."
            ],
            "fun_facts": [
                "You probably have the most organized space among your friend group",
                "People come to you when they need help planning events or projects",
                "You likely remember important dates and details others forget",
                "Your advice is always balanced and well-thought-out"
            ]
        },
        "tongs": {
            "name": "Kitchen Tongs",
            "emoji": "🦞",
            "description": "You're the helper everyone needs! Like tongs, you're incredibly useful, always ready to lend a hand, and can adapt to almost any situation. You're great at bringing people together and helping them reach their goals.",
            "traits": [
                "Always ready to help and assist",
                "Highly adaptable to any situation",
                "Great at handling delicate matters",
                "Natural facilitator and connector"
            ],
            "strengths": [
                "You help others reach their potential",
                "Excellent at handling sensitive situations",
                "Very practical and solution-oriented",
                "People rely on your helpful nature"
            ],
            "compatibility": [
                {"name": "Grill Grates", "emoji": "🔥", "reason": "You're perfect partners for outdoor cooking adventures!"},
                {"name": "Salad Bowl", "emoji": "🥗", "reason": "Great for gently tossing and serving with care!"},
                {"name": "Whisk", "emoji": "🥛", "reason": "Both adaptable tools ready for any kitchen challenge!"}
            ],
            "personality_insights": [
                "You have a special gift for helping others reach their full potential.",
                "You're the friend who always offers to help with everything.",
                "You have a talent for bringing out the best in other people."
            ],
            "fun_facts": [
                "You're probably the friend who always offers to help with everything",
                "You have a talent for bringing out the best in other people",
                "You're likely great at handling delicate or sensitive situations",
                "People feel comfortable opening up to you about personal matters"
            ]
        },
        "spatula": {
            "name": "Spatula",
            "emoji": "🍴",
            "description": "You're the go-to problem solver who can handle any sticky situation! Like a spatula, you're flexible, helpful, and incredibly versatile. You're always there to help others out of tight spots and can adapt to almost any challenge.",
            "traits": [
                "Flexible and adaptable",
                "Helpful and reliable",
                "Problem solver extraordinaire",
                "Gentle touch with delicate situations"
            ],
            "strengths": [
                "You're incredibly adaptable and flexible in any situation",
                "You're always there to help others out of tight spots",
                "You have a gentle touch that can handle delicate tasks",
                "You can turn any situation around"
            ],
            "compatibility": [
                {"name": "Pan", "emoji": "🍳", "reason": "You work together to create perfect results!"},
                {"name": "Bowl", "emoji": "🥣", "reason": "You help each other achieve the perfect mix!"},
                {"name": "Baking Sheet", "emoji": "🍪", "reason": "You're the dynamic duo of baking perfection!"}
            ],
            "personality_insights": [
                "You're incredibly adaptable and flexible in any situation.",
                "You're always there to help others out of tight spots.",
                "You have a gentle touch that can handle delicate tasks."
            ],
            "fun_facts": [
                "Spatulas come in many shapes and sizes for different tasks",
                "The word 'spatula' comes from the Latin 'spatha', meaning 'broad sword'",
                "Silicone spatulas can withstand high temperatures without melting"
            ]
        },
        "grater": {
            "name": "Grater",
            "emoji": "🧀",
            "description": "You're the perfectionist who pays attention to every little detail! Like a grater, you're thorough, patient, and believe that small details make a big difference. You help others achieve the perfect texture and consistency in everything they do.",
            "traits": [
                "Detail-oriented and thorough",
                "Patient and methodical",
                "Perfectionist with high standards",
                "Believes in the power of small details"
            ],
            "strengths": [
                "You have incredible attention to detail",
                "You're patient and thorough in everything you do",
                "You believe that small details make a big difference",
                "You help others achieve perfection"
            ],
            "compatibility": [
                {"name": "Cheese", "emoji": "🧀", "reason": "You bring out the best in each other's flavors!"},
                {"name": "Vegetables", "emoji": "🥕", "reason": "You transform the ordinary into something extraordinary!"},
                {"name": "Citrus", "emoji": "🍋", "reason": "You add the perfect zing to any dish!"}
            ],
            "personality_insights": [
                "You have incredible attention to detail.",
                "You're patient and thorough in everything you do.",
                "You believe that small details make a big difference."
            ],
            "fun_facts": [
                "Graters come in many different sizes for different textures",
                "The microplane grater was originally designed for woodworking",
                "Freshly grated cheese has much better flavor than pre-grated"
            ]
        },
        "colander": {
            "name": "Colander",
            "emoji": "🍝",
            "description": "You're the practical problem solver who knows how to separate what matters! Like a colander, you're great at filtering out the important from the unimportant. You help others stay organized and focused on what truly matters.",
            "traits": [
                "Practical and organized",
                "Great at filtering and sorting",
                "Helps others stay focused",
                "Problem solver with clear thinking"
            ],
            "strengths": [
                "You're great at filtering out what's important from what's not",
                "You have a practical approach to solving problems",
                "You help others stay organized and focused",
                "You bring clarity to confusing situations"
            ],
            "compatibility": [
                {"name": "Pasta", "emoji": "🍝", "reason": "You're the perfect pair for Italian cooking!"},
                {"name": "Vegetables", "emoji": "🥬", "reason": "You help each other stay fresh and clean!"},
                {"name": "Sink", "emoji": "🚰", "reason": "You work together to keep everything flowing smoothly!"}
            ],
            "personality_insights": [
                "You're great at filtering out what's important from what's not.",
                "You have a practical approach to solving problems.",
                "You help others stay organized and focused."
            ],
            "fun_facts": [
                "Colanders have been used since ancient times",
                "The holes in a colander are called 'perforations'",
                "Some colanders have feet so they can stand on the counter"
            ]
        },
        "rolling_pin": {
            "name": "Rolling Pin",
            "emoji": "🥖",
            "description": "You're the steady force that keeps everything rolling smoothly! Like a rolling pin, you're consistent, reliable, and great at smoothing out difficult situations. You have a calming presence that others appreciate and rely on.",
            "traits": [
                "Steady and consistent",
                "Reliable and dependable",
                "Calming presence",
                "Great at smoothing out difficulties"
            ],
            "strengths": [
                "You're incredibly reliable and consistent in your actions",
                "You have a steady, calming presence that others appreciate",
                "You're great at smoothing out difficult situations",
                "You provide stability in uncertain times"
            ],
            "compatibility": [
                {"name": "Dough", "emoji": "🥖", "reason": "You transform raw potential into something beautiful!"},
                {"name": "Pastry Board", "emoji": "🪵", "reason": "You provide the perfect foundation for success!"},
                {"name": "Flour", "emoji": "🌾", "reason": "You work together to create magic from simple ingredients!"}
            ],
            "personality_insights": [
                "You're incredibly reliable and consistent in your actions.",
                "You have a steady, calming presence that others appreciate.",
                "You're great at smoothing out difficult situations."
            ],
            "fun_facts": [
                "Rolling pins have been used for thousands of years",
                "Different cultures have different styles of rolling pins",
                "A good rolling pin should feel comfortable in your hands"
            ]
        },
        "peeler": {
            "name": "Peeler",
            "emoji": "🥕",
            "description": "You're the gentle soul who can peel away layers to reveal the truth! Like a peeler, you're precise, patient, and great at helping others reveal their true selves. You have a gentle approach that makes people feel safe opening up.",
            "traits": [
                "Precise and gentle",
                "Patient and thorough",
                "Helps others reveal their true selves",
                "Careful and considerate approach"
            ],
            "strengths": [
                "You have a gentle, patient approach to life",
                "You're great at helping others reveal their true selves",
                "You're precise and careful in your interactions",
                "You create safe spaces for vulnerability"
            ],
            "compatibility": [
                {"name": "Vegetables", "emoji": "🥕", "reason": "You reveal the beauty hidden beneath the surface!"},
                {"name": "Fruits", "emoji": "🍎", "reason": "You help each other shine in your natural state!"},
                {"name": "Potatoes", "emoji": "🥔", "reason": "You transform the humble into something extraordinary!"}
            ],
            "personality_insights": [
                "You have a gentle, patient approach to life.",
                "You're great at helping others reveal their true selves.",
                "You're precise and careful in your interactions."
            ],
            "fun_facts": [
                "The modern peeler was invented in the 1920s",
                "Different peelers work better for different types of produce",
                "A sharp peeler is much safer than a dull one"
            ]
        }
    }
    
    return utensil_data.get(utensil_type, utensil_data["wooden_spoon"])