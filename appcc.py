import json
import re
from fuzzywuzzy import fuzz

# Load the about_us.json data from the given file path
def load_about_us_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\about_us.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Load the contact_us.json data from the given file path
def load_contact_us_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\contact_us.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Load the faqs.json data from the given file path
def load_faqs_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\faqs.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Load the homepage.json data from the given file path
def load_homepage_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\homepage.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
#Load the media.json data from the given file path
def load_media_data():
    file_path = r"C:/Users/Administrator/Desktop/Garuda/all garuda/data/media.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
def load_products_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\products.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Load the services.json data from the given file path
def load_services_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\services.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
# Load shop.json data from the given file path (new integration)
def load_shop_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\shop.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
# Load the training.json data from the given file path (new integration)
def load_training_data():
    file_path = r"C:\Users\Administrator\Desktop\Garuda\all garuda\data\training.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


# Load all data at the beginning
about_us_data = load_about_us_data()
contact_us_data = load_contact_us_data()
faqs_data = load_faqs_data()
homepage_data = load_homepage_data()
media_data = load_media_data()
products_data = load_products_data()
services_data = load_services_data()
shop_data = load_shop_data()
training_data = load_training_data() 

# Check if the data was loaded successfully
if about_us_data is None or contact_us_data is None or faqs_data is None or homepage_data is None:
    print("Error: Could not load one or more JSON files.")
    exit()

# Define synonyms for keywords
SYNONYMS = {
    "founder": ["agnishwar", "jayaprakash", "agni", "agnish", "ceo", "creator"],
    "co-founder": ["cofounder", "rithika", "mohan", "cio", "rith", "rithu", "partner"],
    "clients": ["partners", "collaborators", "companies", "customers"],
    "vision": ["goal", "future", "objective", "aim"],
    "mission": ["purpose", "plan", "strategy"],
    "about": ["company", "introduction", "history", "profile"],
    "contact": ["contact", "reach", "get in touch", "get contact", "how to reach", "how to contact"],
    "phone": ["phone", "mobile", "contact number", "number", "ph"],
    "email": ["email", "mail", "contact email", "mail id", "garuda mail id", "garuda email id"],
    "address": ["address", "location", "office address", "company address", "where are you located"],
    "faq": ["faq", "frequently asked questions", "questions", "help", "ask"],
    "brand ambassador": ["ambassador", "ms dhoni", "dhoni", "cricketer", "celebrity"],
    "kisan drone": ["kisan drone", "agri drone", "farm drone", "precision agriculture", "agriculture drone"],
    "subsidy": ["subsidy", "government support", "financial aid", "ministry subsidy"],
    "impact": ["impact", "results", "outcome", "achievements", "metrics"],
    "ceo message": ["ceo message", "ceo quote", "agnishwar's message", "founder's message"],
    "women empowerment": ["women empowerment", "namo drone didis", "women-led initiative", "women in agriculture"],
    "innovation": ["innovation", "tech-led nation", "applications", "agriculture", "defense", "surveillance"],
    "surveillance drone": ["surveillance drone", "monitoring drone", "security drone", "reconnaissance drone"],
    "mapping drone": ["mapping drone", "survey drone", "aerial survey drone", "surveying drone"],
    "solar panel cleaning drone": ["solar panel cleaning drone", "solar panel cleaning", "solar drone"],
    "seed dropping drone": ["seed dropping drone", "seed sowing drone", "agriculture seed drone"],
    "submarine": ["submarine drone", "underwater drone", "marine drone"],
    "boat": ["water cleaning boat", "cleaning boat", "debris collection boat"],
    "ugv": ["ugv", "unmanned ground vehicle", "ground vehicle", "robotic ground vehicle"],
    "fixed wing drone": ["fixed wing drone", "fixed wing vtol", "vtol drone"],
    "industry 4.0 drone": ["industry 4.0 drone", "smart drone", "industrial drone"],
    "stringing drone": ["stringing drone", "power line drone", "cable drone"],
    "shop": ["shop", "store", "buy", "purchase", "products", "items", "garuda shop"],
    "shop products": ["shop products", "store products", "shop items", "store items", "garuda products"],
    "cart": ["cart", "shopping cart", "purchase cart"],
    "order": ["order", "buy now", "place order", "checkout"],
    "training": ["training", "courses", "learn", "drone pilot training", "remote pilot training", "DGCA certification", "RPTO", "garuda training"],
    "center of excellence": ["center of excellence", "coe", "establish coe", "drone education", "higher education institutions"],
    "course details": ["course details", "course information", "training course", "course A", "course B", "course C", "course D"],
    "uav research": ["uav research", "drone research", "research center", "unmanned aerial vehicle research"]
}

# Function to normalize user input for synonym matching
def normalize_message(message):
    normalized_words = []
    for word in message.lower().split():
        for key, synonyms in SYNONYMS.items():
            if word in synonyms:
                normalized_words.append(key)
                break
        else:
            normalized_words.append(word)
    return " ".join(normalized_words)

# Function to handle greetings
def greet_user(message):
    greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
    if any(greeting in message.lower() for greeting in greetings):
        return "Hello! I'm Garuda, your friendly bot. How can I assist you today?"
    return None

# Function to handle name detection
def detect_name(message):
    match = re.search(r"(my name is|i am|myself) (\w+)", message.lower())
    if match:
        user_name = match.group(2)
        return f"Hello, {user_name}! Nice to meet you."
    return None

# Function to handle help queries
def offer_help(message):
    if 'help' in message.lower():
        return "Sure! How can I assist you today? You can ask me anything."
    return None

# Function to handle goodbye messages
def say_goodbye(message):
    if 'bye' in message.lower() or 'exit' in message.lower() or 'quit' in message.lower():
        return "Goodbye! Have a great day!"
    return None

# Function to handle 'about us' queries
def handle_about_us(message):
    if "about" in message:
        return about_us_data["about_us"]["introduction"]["description"]
    return None

# Function to handle vision and mission queries
def handle_vision_mission(message):
    if "vision" in message:
        return about_us_data["about_us"]["vision"]
    elif "mission" in message:
        return about_us_data["about_us"]["mission"]
    return None

# Function to handle founder-specific queries
def handle_founder_query(message):
    if "founder" in message and "co" not in message:
        return (f"The Founder & CEO of Garuda is Agnishwar Jayaprakash.\n"
                f"Background: {about_us_data['about_us']['leadership']['agnishwar_jayaprakash']['background']}\n"
                f"Quote: \"{about_us_data['about_us']['leadership']['agnishwar_jayaprakash']['quote']}\"")
    elif "co-founder" in message or "cio" in message:
        return (f"The Co-Founder & CIO of Garuda is Rithika Mohan.\n"
                f"Background: {about_us_data['about_us']['leadership']['rithika_mohan']['background']['education']}, "
                f"{about_us_data['about_us']['leadership']['rithika_mohan']['background']['experience']}\n"
                f"Quote: \"{about_us_data['about_us']['leadership']['rithika_mohan']['quote']}\"")
    return None

# Function to handle clients and partners queries
def handle_clients_and_partners_query(message):
    if "clients" in message:
        clients = ', '.join(about_us_data['about_us']['introduction']['clients_and_partners'])
        return f"Our clients and partners include: {clients}."
    return None

# Function to handle contact details queries
def handle_contact_query(message):
    if "phone" in message:
        return f"Here are our contact numbers: {', '.join(contact_us_data['contact_info']['phone_numbers'])}"
    elif "email" in message:
        return f"Here are our contact emails: {', '.join(contact_us_data['contact_info']['emails'])}"
    elif "address" in message:
        return (f"Our office is located at: {contact_us_data['contact_info']['address']}\n"
                f"You can view the location on the map here: https://maps.app.goo.gl/W8qCJfdS9HEbtrP57")
    elif "contact" in message:
        return (f"Here are the contact details:\n"
                f"Phone: {', '.join(contact_us_data['contact_info']['phone_numbers'])}\n"
                f"Email: {', '.join(contact_us_data['contact_info']['emails'])}\n"
                f"Address: {contact_us_data['contact_info']['address']}\n"
                f"View on the map: https://maps.app.goo.gl/W8qCJfdS9HEbtrP57")
    return None

# Function to handle homepage-related queries
def handle_homepage_query(message):
    if "brand ambassador" in message:
        return f"The Brand Ambassador of Garuda Aerospace is {homepage_data['home_page']['brand_ambassador']['name']}.\n" \
               f"Quote: \"{homepage_data['home_page']['brand_ambassador']['quote']}\""
    elif "kisan drone" in message:
        drone_info = homepage_data['home_page']['kisan_agri_drone']
        return f"Kisan/Agri Drone: {drone_info['description']}\n" \
               f"Advantages: {', '.join(drone_info['advantages'])}\n" \
               f"Subsidy details: Provided by {drone_info['subsidy']['provided_by']}.\n" \
               f"Details: {drone_info['subsidy']['details']}"
    elif "impact" in message:
        impact = homepage_data['home_page']['impact']
        return f"Impact:\n" \
               f"Kilometers Travelled: {impact['kilometers_travelled']}\n" \
               f"Projects: {impact['projects']}\n" \
               f"Districts Covered: {impact['districts_covered']}\n" \
               f"Centers of Excellence: {impact['centers_of_excellence']}\n" \
               f"Partners: {impact['partners']}\n" \
               f"Rural Youth Trained/Jobs Created: {impact['rural_youth_trained_or_jobs_created']}\n" \
               f"Vans Deployed: {impact['vans_deployed']}\n" \
               f"Drones Distributed: {impact['drones_distributed']}"
    elif "ceo message" in message:
        ceo_message = homepage_data['home_page']['ceo_message']
        return f"Message from the CEO, {ceo_message['name']}:\n" \
               f"Quote: \"{ceo_message['quote']}\""
    elif "women empowerment" in message:
        women_empowerment = homepage_data['home_page']['women_empowerment_initiative']
        return f"{women_empowerment['program_name']}:\n" \
               f"{women_empowerment['scheme_description']}\n" \
               f"Details: {', '.join(women_empowerment['details'])}"
    elif "innovation" in message:
        innovations = homepage_data['home_page']['innovations']
        return f"Innovation: {innovations['tagline']}\n" \
               f"Applications: {', '.join(innovations['applications'])}"
    return None

#Function to handle media-related queries
def handle_media_query(message):
    if "media" in message or "news" in message or "articles" in message:
        media_list = media_data['media']
        response = "Here are some of the latest media articles:\n"
        for article in media_list:
            response += f"\nTitle: {article['title']}\n" \
                        f"Author: {article['author']}\n" \
                        f"Date: {article['date']}\n" \
                        f"Content: {article['content'][:200]}...\n"  # Displaying first 200 chars of content
            if article['quotes']:
                response += f"Quote: {article['quotes'][0]['author']} said, \"{article['quotes'][0]['quote']}\"\n"
        return response
    return None

# Function to handle product-related queries
def handle_product_query(message):
    # First check if the user directly asks about products
    if 'product' in message or 'products' in message or 'items' in message:
        product_list = "Here are some of the products we offer:\n"
        for product in products_data['products']:
            product_list += f"\nTitle: {product['title']}\nDescription: {product['description']}"
            if 'features' in product:
                product_list += f"\nFeatures: {', '.join(product['features'])}"
            if 'uses' in product:
                product_list += f"\nUses: {', '.join(product['uses'])}\n"
        return product_list.strip()
    
    # Fuzzy matching for product name (if specific product is mentioned)
    for product in products_data['products']:
        if fuzz.partial_ratio(product['title'].lower(), message.lower()) > 70:
            product_info = f"Title: {product['title']}\nDescription: {product['description']}"
            if 'features' in product:
                product_info += f"\nFeatures: {', '.join(product['features'])}"
            if 'uses' in product:
                product_info += f"\nUses: {', '.join(product['uses'])}"
            return product_info
    return None

def handle_services_query(message):
    # Normalize the user message for matching keywords
    if 'industrial services' in message.lower():
        return services_data['services']['industrial_services']['description']
    elif 'agriculture' in message.lower():
        return services_data['services']['agriculture']['description']
    elif 'disaster management' in message.lower():
        return services_data['services']['disaster_management']['description']
    elif 'anti-drone system' in message.lower():
        return services_data['services']['anti_drone_system']['description']
    elif 'delivery load carrying' in message.lower():
        return services_data['services']['delivery_load_carrying']['description']
    elif 'warehouse management' in message.lower():
        return services_data['services']['warehouse_management']['description']
    elif 'project management' in message.lower():
        return services_data['services']['project_management_structural_inspection']['description']
    elif 'highway traffic monitoring' in message.lower():
        return services_data['services']['highway_traffic_monitoring']['description']
    elif 'mapping services' in message.lower():
        return services_data['services']['mapping_services']['description']
    elif 'internal boiler inspection' in message.lower():
        return services_data['services']['internal_boiler_inspection']['description']
    elif 'chimney stack inspection' in message.lower():
        return services_data['services']['chimney_stack_inspection']['description']
    elif 'solar panel inspection' in message.lower():
        return services_data['services']['solar_panel_inspection_cleaning']['description']
    elif 'structural damage assessment' in message.lower():
        return services_data['services']['structural_damage_assessment']['description']
    elif 'thermography drone' in message.lower():
        return services_data['services']['thermography_drone']['description']
    elif 'lidar analysis' in message.lower():
        return services_data['services']['lidar_analysis']['description']
    elif 'wind turbine inspection' in message.lower():
        return services_data['services']['wind_turbine_inspection']['description']
    elif 'mining site inspection' in message.lower():
        return services_data['services']['mining_site_inspection']['description']
    elif 'powerline inspection' in message.lower():
        return services_data['services']['powerline_inspection_stringing']['description']
    elif 'environmental impact assessment' in message.lower():
        return services_data['services']['environmental_impact_assessment']['description']
    else:
        return "Sorry, I couldn't find the service you are asking about."
    

# Function to handle shop-specific queries
def handle_shop_query(message):
    if "shop" in message or "products" in message:
        return f"Check out our latest products in the Garuda Shop: {shop_data['shop']['products_url']}"
    elif "order" in message:
        return "You can place your order at our online store. Please visit our shop to explore more."
    return None

def handle_training_query(message):
    if "training" in message or "courses" in message:
        return f"Garuda Aerospace offers a variety of training programs. You can explore our courses here: {training_data['training']['RemotePilotTrainingOrganization']['courses_url']}"
    elif "remote pilot" in message or "rpto" in message:
        return f"Garuda Aerospace offers DGCA-approved Remote Pilot Training Organization (RPTO) courses. We provide comprehensive training for drone pilots."
    elif "center of excellence" in message:
        return (f"Our Center of Excellence (CoE) focuses on building a strong drone ecosystem. "
                f"Learn more about the CoE and its offerings: {training_data['training']['CenterOfExcellence']['features_url']}")
    return None



# Main function to get bot response
def get_bot_response(user_message):
    user_message_normalized = normalize_message(user_message)
    
    response = greet_user(user_message_normalized)
    if response:
        return response

    response = detect_name(user_message_normalized)
    if response:
        return response

    response = offer_help(user_message_normalized)
    if response:
        return response

    response = say_goodbye(user_message_normalized)
    if response:
        return response

    response = handle_about_us(user_message_normalized)
    if response:
        return response

    response = handle_vision_mission(user_message_normalized)
    if response:
        return response

    response = handle_founder_query(user_message_normalized)
    if response:
        return response

    response = handle_clients_and_partners_query(user_message_normalized)
    if response:
        return response

    response = handle_contact_query(user_message_normalized)
    if response:
        return response

    response = handle_homepage_query(user_message_normalized)
    if response:
        return response
    
    response = handle_media_query(user_message_normalized)
    if response:
        return response

    # Check for product-related queries first
    response = handle_product_query(user_message_normalized)
    if response:
        return response
    
    # Function to handle service-related queries
    response = handle_services_query(user_message_normalized)
    if response:
        return response
    
    # Check for shop-related intents
    response = handle_shop_query(user_message_normalized)
    if response:
        return response
    
    # Check for training-related queries
    response = handle_training_query(user_message_normalized)
    if response:
        return response

    return "Sorry, I didn't quite understand that. Could you please rephrase?"

# Example usage
while True:
    user_message = input("You: ")
    response = get_bot_response(user_message)
    print("Bot:", response)
    if 'bye' in user_message.lower():
        break

