
# Expected functions (minimum): 
# def add_library_branch(branch_id, location, operating_hours) 
# def add_book(isbn, title, author, genre, copies, book_type) 
# def register_member(member_id, name, contact, membership_type) 
# def issue_book(member_id, isbn, branch_id) 
# def return_book(member_id, isbn, return_date, condition) 
# def calculate_fine(member_id, return_date, due_date) 
# def add_to_waitlist(member_id, isbn) 
# def generate_recommendations(member_id, recommendation_count) 
# def analyze_reading_patterns(member_id) 
# def generate_popular_books_report(time_period, genre) 
# def track_reading_challenge(member_id, challenge_type




ef add_library_branch(branch_id, location, operating_hours):

    library_branches[branch_id]={
        "location": location,
        "operating_hours": operating_hours
    }
    print(f"Branch {branch_id} at {location} added Successfully.")

def add_library_branches():
    print("Add a new Library Branch:")
    while True:
        branch_id= input("Enter branch id: ").strip()
        if branch_id in library_branches:
            print(f"{branch_id} already exists!")
            continue
        location= input("Enter location: ").strip()
        operating_hours= input("Enter operating hours: ").strip()
    
        add_library_branch(branch_id, location, operating_hours)

        cont= input("Add another branch? (yes/no): ").strip().lower()
        if cont !='yes':
            break