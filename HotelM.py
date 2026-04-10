from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hotel: Hello! How can I assist you today?",
        "hi": "Hotel: Hello! How can I assist you today?",
        "hey": "Hotel: Hey there! How can I help you?",
        "good morning": "Hotel: Good morning! Welcome to Hotel RegX. How can I assist you?",
        "good evening": "Hotel: Good evening! Welcome to Hotel RegX. How may I help you?",
        "good night": "Hotel: Good night! If you need anything, our front desk is available 24/7.",

        # Booking
        "book": "Hotel: You can book a room through our website or by calling our reservation line at (123) 456-7890.",
        "booking": "Hotel: To make a booking, visit our website or call (123) 456-7890. We accept reservations up to 6 months in advance.",
        "reservation": "Hotel: Reservations can be made online or by phone. We recommend booking early for peak seasons.",
        "reserve": "Hotel: You can reserve a room by calling (123) 456-7890 or emailing Hotel123@gmail.com.",
        "availability": "Hotel: Please provide your desired dates for availability information. You can also check online at our website.",
        "available": "Hotel: Room availability depends on the season. Please share your check-in and check-out dates.",
        "group booking": "Hotel: For group bookings of 5 or more rooms, please contact our reservations team for special group rates.",
        "early booking": "Hotel: We offer early bird discounts for bookings made 30+ days in advance!",

        # Rooms
        "room": "Hotel: We have Standard Rooms, Deluxe Rooms, Premium Suites, and Presidential Suites.",
        "rooms": "Hotel: Our rooms range from cozy Standard Rooms to luxurious Presidential Suites. Which type interests you?",
        "suite": "Hotel: Our suites include a living area, king-size bed, jacuzzi, and a stunning city view.",
        "deluxe": "Hotel: Deluxe Rooms feature a king or twin bed, flat-screen TV, minibar, and garden view.",
        "standard room": "Hotel: Standard Rooms include a queen bed, flat-screen TV, air conditioning, and en-suite bathroom.",
        "presidential": "Hotel: Our Presidential Suite features 2 bedrooms, a private kitchen, butler service, and panoramic views.",
        "single room": "Hotel: Single rooms are available with a comfortable single bed, work desk, and all basic amenities.",
        "double room": "Hotel: Double rooms have a large double bed, wardrobe, flat-screen TV, and private bathroom.",
        "twin room": "Hotel: Twin rooms have two single beds — perfect for friends or colleagues traveling together.",
        "family room": "Hotel: Our Family Rooms accommodate up to 2 adults and 2 children with bunk beds and extra space.",
        "connecting room": "Hotel: Yes, we offer connecting rooms for families or groups who need adjoining accommodations.",
        "balcony": "Hotel: Several of our rooms come with private balconies offering garden or city views.",
        "view": "Hotel: We offer rooms with city views, garden views, pool views, and mountain views depending on availability.",
        "floor": "Hotel: We have 12 floors. Higher floors offer better views and are available at a slight premium.",
        "bed": "Hotel: We offer single, double, queen, and king-size beds. Let us know your preference while booking.",
        "pillow": "Hotel: We offer a pillow menu with soft, firm, memory foam, and hypoallergenic options.",
        "room size": "Hotel: Standard rooms are 30 sqm, Deluxe rooms 45 sqm, Suites 80 sqm, and Presidential Suite 160 sqm.",

        # Check-in / Check-out
        "check-in": "Hotel: Check-in is at 3:00 PM. Early check-in may be available on request subject to availability.",
        "check in": "Hotel: Check-in time is 3:00 PM. Please carry a valid photo ID and your booking confirmation.",
        "check-out": "Hotel: Check-out is at 11:00 AM. Late check-out can be arranged for an additional charge.",
        "check out": "Hotel: Check-out is at 11:00 AM. Please inform the front desk if you need a late check-out.",
        "early check-in": "Hotel: Early check-in is available from 12:00 PM for an extra charge, subject to availability.",
        "late check-out": "Hotel: Late check-out up to 2:00 PM is available for a small fee. Please request in advance.",
        "express checkout": "Hotel: Yes, we offer express checkout. You can settle your bill the night before and drop the key card at the front desk.",

        # Pricing
        "price": "Hotel: Room prices start at Rs.3,500/night for Standard, Rs.6,000 for Deluxe, Rs.12,000 for Suites.",
        "cost": "Hotel: Costs vary by room type and season. Standard rooms start at Rs.3,500/night.",
        "rate": "Hotel: Our nightly rates: Standard Rs.3,500, Deluxe Rs.6,000, Suite Rs.12,000, Presidential Rs.25,000.",
        "rates": "Hotel: Our rates are competitive and include complimentary breakfast and Wi-Fi.",
        "charges": "Hotel: Room charges exclude taxes. GST of 12% is applicable on all bookings.",
        "fee": "Hotel: There are no hidden fees. All charges including taxes are displayed at checkout.",
        "expensive": "Hotel: We offer rooms for every budget. Our Standard Rooms start at just Rs.3,500/night.",
        "cheap": "Hotel: Our most affordable option is the Standard Room at Rs.3,500/night with all essential amenities.",
        "budget": "Hotel: For budget stays, our Standard Rooms at Rs.3,500/night are a great choice!",

        # Payment
        "payment": "Hotel: We accept all major credit/debit cards, cash, UPI, net banking, and mobile wallets.",
        "pay": "Hotel: You can pay online during booking or at the hotel via card, cash, or UPI.",
        "credit card": "Hotel: We accept Visa, Mastercard, American Express, and RuPay cards.",
        "upi": "Hotel: Yes, we accept UPI payments including GPay, PhonePe, and Paytm.",
        "cash": "Hotel: Yes, cash payments are accepted at the front desk in INR.",
        "invoice": "Hotel: A detailed GST invoice will be emailed to you upon check-out.",
        "receipt": "Hotel: Receipts are provided at checkout. You can also request a digital copy via email.",
        "deposit": "Hotel: A refundable security deposit of Rs.2,000 is collected at check-in and returned upon check-out.",

        # Cancellation
        "cancel": "Hotel: Free cancellation is available up to 24 hours before arrival. Cancellations after that incur one night's charge.",
        "cancellation": "Hotel: Our cancellation policy: Free up to 24 hours before check-in, 1 night charge after that.",
        "refund": "Hotel: Refunds for eligible cancellations are processed within 5-7 working days to the original payment method.",
        "no show": "Hotel: In case of a no-show, the full booking amount will be charged.",
        "modify": "Hotel: You can modify your booking up to 48 hours before arrival at no extra charge.",
        "reschedule": "Hotel: Rescheduling is allowed up to 48 hours before check-in. Please call us to modify your dates.",

        # Amenities & Facilities
        "amenities": "Hotel: We offer a fitness center, spa, swimming pool, fine dining, free Wi-Fi, and concierge services.",
        "facilities": "Hotel: Facilities include a gym, pool, spa, business center, conference hall, kids' play area, and more.",
        "wifi": "Hotel: Complimentary high-speed Wi-Fi (100 Mbps) is available throughout the hotel.",
        "wi-fi": "Hotel: Free Wi-Fi is available in all rooms and common areas with speeds up to 100 Mbps.",
        "internet": "Hotel: High-speed internet is complimentary for all guests. Ask the front desk for the password.",
        "pool": "Hotel: Our outdoor heated swimming pool is open from 7:00 AM to 10:00 PM daily.",
        "swimming": "Hotel: We have an outdoor pool and a separate kids' pool. Towels and chairs are provided.",
        "gym": "Hotel: Our fitness center is open 24/7 and equipped with cardio machines, free weights, and yoga mats.",
        "fitness": "Hotel: The fitness center is fully equipped and available to all guests at no extra charge.",
        "workout": "Hotel: Our gym is open 24 hours. Personal training sessions can also be arranged on request.",
        "spa": "Hotel: Our spa offers massages, facials, body scrubs, and aromatherapy. Open 9:00 AM to 9:00 PM.",
        "massage": "Hotel: We offer Swedish, deep tissue, hot stone, and Ayurvedic massages. Book at the spa desk.",
        "sauna": "Hotel: Yes, we have a steam room and sauna available for guests adjacent to the spa.",
        "jacuzzi": "Hotel: Jacuzzis are available in our Suite and Presidential Suite rooms.",
        "parking": "Hotel: Complimentary valet parking is available for all hotel guests.",
        "valet": "Hotel: Yes, valet parking is complimentary. Drive up to the main entrance and our staff will assist.",
        "laundry": "Hotel: Same-day laundry and dry-cleaning services are available. Drop your clothes by 9:00 AM.",
        "dry cleaning": "Hotel: Dry-cleaning services are available and typically returned within 24 hours.",
        "ironing": "Hotel: Ironing boards and irons are available in all rooms. We also offer pressing services.",
        "atm": "Hotel: There is an ATM in the lobby on the ground floor, available 24/7.",
        "currency": "Hotel: Currency exchange services are available at the front desk.",
        "locker": "Hotel: In-room electronic safes are provided in all room types.",
        "safe": "Hotel: Each room has a personal electronic safe for storing valuables.",
        "elevator": "Hotel: We have 4 high-speed elevators serving all 12 floors.",
        "lift": "Hotel: High-speed lifts are available on both the east and west wings.",
        "wheelchair": "Hotel: Our hotel is fully wheelchair accessible with ramps, wide corridors, and accessible rooms.",
        "accessible": "Hotel: We have specially designed accessible rooms and facilities for guests with disabilities.",
        "pet": "Hotel: We are a pet-friendly hotel. Pets up to 10 kg are allowed with a refundable pet deposit.",
        "pets": "Hotel: Pets are welcome! Please inform us in advance. A pet fee of Rs.500/night applies.",
        "smoking": "Hotel: Our hotel is entirely non-smoking. Designated smoking zones are available on the terrace.",
        "non-smoking": "Hotel: All rooms are non-smoking. Smoking is only permitted in designated outdoor areas.",
        "air conditioning": "Hotel: All rooms have individual climate-controlled air conditioning.",
        "heater": "Hotel: All rooms are equipped with heating facilities for the winter season.",
        "minibar": "Hotel: Deluxe rooms and above come with a stocked minibar. Items are charged to your room.",
        "kettle": "Hotel: An electric kettle with complimentary tea and coffee is available in all rooms.",
        "television": "Hotel: All rooms feature a 55-inch flat-screen smart TV with streaming and satellite channels.",
        "tv": "Hotel: Our rooms have 55-inch smart TVs with Netflix, Prime Video, and 100+ satellite channels.",

        # Food & Dining
        "restaurant": "Hotel: Yes, we have a restaurant serving all meals.",
        "food": "Hotel: We offer in-room dining, buffet breakfast, and a la carte dining at our restaurant.",
        "dining": "Hotel: Fine dining is available at The Regency Table. Reservations recommended for dinner.",
        "breakfast": "Hotel: Complimentary buffet breakfast is served from 7:00 AM to 10:30 AM daily.",
        "lunch": "Hotel: Lunch is served from 12:30 PM to 3:00 PM at our restaurant.",
        "dinner": "Hotel: Dinner is served from 7:00 PM to 11:00 PM. We recommend reserving a table.",
        "buffet": "Hotel: Breakfast buffet is complimentary. Lunch and dinner buffets are available on weekends.",
        "room service": "Hotel: 24-hour room service is available. Our menu covers snacks, meals, and beverages.",
        "menu": "Hotel: Our menu includes Indian, Continental, Asian, and Mediterranean dishes.",
        "vegetarian": "Hotel: Yes, we have an extensive vegetarian and vegan menu available.",
        "vegan": "Hotel: We offer dedicated vegan options. Please inform us of dietary preferences in advance.",
        "allergy": "Hotel: Please inform our staff of any food allergies. Our chefs accommodate dietary restrictions.",
        "bar": "Hotel: Our rooftop bar Sky Lounge is open from 5:00 PM to 12:00 AM with signature cocktails.",
        "cafe": "Hotel: Brewed Awakenings cafe is open from 7:00 AM to 11:00 PM serving coffee, snacks, and pastries.",
        "coffee": "Hotel: Complimentary tea and coffee are available in your room. Our cafe serves premium brews.",
        "alcohol": "Hotel: Alcohol is served at our Sky Lounge bar. In-room alcohol can be ordered via room service.",
        "water": "Hotel: Complimentary bottled water is provided daily. Additional bottles can be requested.",

        # Services
        "services": "Hotel: We offer room service, laundry, and concierge services.",
        "concierge": "Hotel: Our concierge team is available 24/7 to assist with travel, tours, reservations, and more.",
        "baby": "Hotel: Babysitting services are available on request. Please inform us 4 hours in advance.",
        "kids": "Hotel: We have a kids play area, children's pool, and babysitting services for families.",
        "crib": "Hotel: Baby cribs and high chairs are available on request at no extra charge.",
        "wake up": "Hotel: Wake-up call service is available. You can request it at the front desk or dial 0 from your room.",
        "newspaper": "Hotel: Complimentary newspapers are delivered to your room every morning.",
        "housekeeping": "Hotel: Housekeeping is done daily between 9:00 AM and 1:00 PM. You can request extra service anytime.",
        "clean": "Hotel: Rooms are cleaned daily. For immediate service, dial housekeeping from your room phone.",
        "towel": "Hotel: Fresh towels are provided daily. Extra towels can be requested from housekeeping.",
        "toiletries": "Hotel: We provide premium toiletries including shampoo, conditioner, body wash, and dental kit.",
        "extra bed": "Hotel: Extra beds are available for Rs.1,000/night. Suitable for children up to 12 years.",
        "rollaway": "Hotel: Rollaway beds are available on request for a charge of Rs.1,000/night.",

        # Transportation
        "transport": "Hotel: We offer airport transfers, local sightseeing tours, and car rental services.",
        "transportation": "Hotel: We offer airport shuttle services and car rentals.",
        "airport": "Hotel: Airport shuttle runs every 2 hours. Private transfers can be arranged on request.",
        "shuttle": "Hotel: Our complimentary shuttle runs to the airport and major city landmarks twice daily.",
        "taxi": "Hotel: Our concierge can arrange taxis and cabs at any time. Please contact the front desk.",
        "cab": "Hotel: Cab services are available 24/7 through our concierge.",
        "car rental": "Hotel: We partner with leading car rental agencies. Ask our travel desk for options and rates.",
        "tour": "Hotel: We offer guided city tours, heritage walks, and day trips. Ask our travel desk for packages.",
        "sightseeing": "Hotel: Our travel desk can arrange sightseeing tours to local attractions, monuments, and markets.",

        # Events & Conferences
        "event": "Hotel: We can host events. Please contact our event coordinator for more details.",
        "events": "Hotel: Our event spaces can accommodate 10 to 500 guests. Contact us for customized packages.",
        "wedding": "Hotel: We offer elegant wedding packages with catering, decor, and coordination services.",
        "conference": "Hotel: Our conference hall seats 200 guests and is equipped with AV, projector, and video conferencing.",
        "meeting": "Hotel: Meeting rooms for 10-30 people are available with projectors and high-speed internet.",
        "banquet": "Hotel: Our banquet hall accommodates up to 300 guests for dinners, receptions, and celebrations.",
        "corporate": "Hotel: We offer special corporate rates and packages for business travelers and company events.",
        "business": "Hotel: Our business center is open 24/7 with computers, printers, and private workstations.",
        "projector": "Hotel: Projectors, screens, and PA systems are available in all conference and meeting rooms.",

        # Contact & Location
        "contact": "Hotel: You can contact us at (123) 456-7890 or email us at Hotel123@gmail.com",
        "phone": "Hotel: Our front desk number is (123) 456-7890. We are available around the clock.",
        "call": "Hotel: You can call us at (123) 456-7890 anytime. We're happy to help!",
        "email": "Hotel: You can email us at Hotel123@gmail.com",
        "address": "Hotel: We are located at 123 Main Street.",
        "location": "Hotel: Hotel RegX is at 123 Main Street, City Center — 10 minutes from the airport.",
        "directions": "Hotel: We are 10 km from the airport and 2 km from the central railway station.",
        "nearby": "Hotel: Nearby attractions include City Mall (500m), Heritage Museum (1.2 km), and Central Park (800m).",
        "distance": "Hotel: We are 10 km from the airport, 2 km from the railway station, and 500m from the metro.",

        # Branches
        "branch": "Hotel: We have branches in Lucknow, Delhi, and Goa.",
        "branches": "Hotel: We have branches in Lucknow, Delhi, and Goa.",
        "lucknow": "Hotel: Our Lucknow branch is located at MG Road, near Hazratganj. Call (522) 111-2222.",
        "delhi": "Hotel: Our Delhi branch is in Connaught Place. Call (011) 333-4444 for reservations.",
        "goa": "Hotel: Our Goa branch is near Baga Beach — perfect for a beach holiday! Call (832) 555-6666.",

        # Offers & Loyalty
        "offer": "Hotel: We have seasonal offers. Please check our website.",
        "discount": "Hotel: Members get 15% off on room bookings. Sign up for our loyalty program today!",
        "deal": "Hotel: Weekend deals include complimentary breakfast and late check-out. Check our website.",
        "promo": "Hotel: Use promo code REGX10 for 10% off your first booking!",
        "honeymoon": "Hotel: Our Honeymoon Package includes a decorated room, rose bath, candle-lit dinner, and spa session.",
        "anniversary": "Hotel: Celebrate your anniversary with our special package — includes room upgrade and complimentary cake.",
        "loyalty": "Hotel: Yes, we have a loyalty program that offers exclusive benefits and discounts.",
        "membership": "Hotel: Join RegX Rewards for free — earn 10 points per Rs.100 spent and enjoy exclusive perks.",
        "points": "Hotel: RegX Rewards members earn 10 points per Rs.100. 1000 points = Rs.500 off on your next stay.",
        "voucher": "Hotel: Gift vouchers are available at the front desk and can be used for rooms, dining, and spa.",

        # Feedback & Complaints
        "feedback": "Hotel: We value your feedback! Please share your experience with us.",
        "review": "Hotel: Thank you for considering a review! Your experience matters to us.",
        "complaint": "Hotel: We're sorry to hear that. Please provide details of your complaint.",
        "problem": "Hotel: We apologize for the inconvenience. Please describe the issue and we'll resolve it right away.",
        "issue": "Hotel: Please let us know the issue and our team will attend to it within 15 minutes.",
        "manager": "Hotel: You can request to speak with the duty manager at any time by calling the front desk.",
        "improve": "Hotel: We are always looking to improve. Your suggestions are welcome via our feedback form.",

        # Miscellaneous
        "age": "Hotel: Guests must be 18 years or older to check in independently.",
        "id": "Hotel: A valid government-issued photo ID (Passport, Aadhaar, Driving License) is required at check-in.",
        "passport": "Hotel: Foreign nationals must present their passport and visa for check-in.",
        "lost": "Hotel: If you have lost an item, please contact our housekeeping department at extension 101.",
        "found": "Hotel: Lost and found items are kept for 30 days. Contact us at Hotel123@gmail.com to claim.",
        "noise": "Hotel: Quiet hours are observed from 11:00 PM to 7:00 AM. We appreciate your cooperation.",
        "party": "Hotel: In-room parties are not permitted. Our event spaces are available for celebrations.",
        "security": "Hotel: We have 24/7 CCTV surveillance, security personnel, and key card access on all floors.",
        "emergency": "Hotel: In case of emergency, dial 999 from your room phone. Our team is available around the clock.",
        "fire": "Hotel: Fire exits are clearly marked on every floor. Please review the safety card in your room.",
        "doctor": "Hotel: A doctor on call is available 24/7. Please contact the front desk for medical assistance.",
        "medical": "Hotel: We have a first-aid room and a doctor on call. Dial 0 from your room for assistance.",
        "pharmacy": "Hotel: A pharmacy is available within the hotel premises on the ground floor.",
        "prayer": "Hotel: A prayer room and meditation room is available on the 2nd floor for all guests.",
        "library": "Hotel: We have a reading lounge with books, magazines, and newspapers on the 1st floor.",
        "gift": "Hotel: Gift vouchers and hotel merchandise are available at the reception desk.",
        "souvenir": "Hotel: A souvenir shop is located near the lobby with local crafts and hotel merchandise.",
        "music": "Hotel: Live music is performed at our Sky Lounge every Friday and Saturday from 7 PM.",
        "entertainment": "Hotel: We offer live music, cultural performances, and movie nights in our event lawn.",
        "pool table": "Hotel: Yes, we have a billiards table in our recreation lounge on the 3rd floor.",
        "games": "Hotel: Our recreation lounge has board games, billiards, and a gaming console area.",

        "bye": "Hotel: Goodbye! Have a great day!",
        "goodbye": "Hotel: Thank you for reaching out! Safe travels and see you soon at Hotel RegX!",
        "thank you": "Hotel: You're most welcome! Is there anything else I can help you with?",
        "thanks": "Hotel: Happy to help! Let us know if you need anything else.",
    }

    if user_input == "bye":
        return "Hotel: Goodbye! Have a great day!"

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Hotel: Sorry, I didn't understand that. Please rephrase."

@app.route("/")
def home():
    return send_from_directory('.','test.html')
@app.route("/home.html")
def home_page():
    return send_from_directory('.', 'test.html')

@app.route("/about.html")
def about_page():
    return send_from_directory('.', 'test.html')

@app.route("/form.html")
def form_page():
    return send_from_directory('.', 'test.html')

@app.route("/chat",methods=["POST"])
def chat():
    data=request.json
    user_message=data.get("message")
    response=get_response(user_message)
    return jsonify({"response": response})

if __name__ =="__main__":
    print("Chatbot is running! Visit http://127.0.0.1:5000 in your browser")
    print("Serving index.html file")
    app.run(debug=True)
