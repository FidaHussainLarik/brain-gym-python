from bs4 import BeautifulSoup


from pathlib import Path
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

with open(DATA_DIR / "home.html") as html_file:
    content = html_file.read()

    #Print raw html content
    print("\n\n---- 1️  Print content of raw html ----\n")
    # print(content)

    # Read -> parse -> review.
    # Keep comments short so the important steps stand out.
    soup = BeautifulSoup(content, "lxml")
    # print(pretier version of the same content)
    print("\n\n---- 2️  Print content of BeautSoup object ----\n\n")
    # print(soup.prettify())

    

    print("\n\n---- 3️  Parsing <h5> tags ----\n\n")
    courses_html_tags = soup.find_all("h5")

    # Numbered output makes quick review easier.
    # for index, tag in enumerate(courses_html_tags, start=1):
        # print(f"{index}. {tag}")

    # extracting tag headings
    # print("\n\nCourses on the webpage\n\n")
    # for index, tag in enumerate(courses_html_tags, start=1):
    #         print(f"{index}. {tag.text}")

    print("\n\n---- 4️ Parsing <div> tags ----\n\n")


    course_cards = soup.find_all('div',class_ = 'card')

    # Will return the entire 'div' tag code
    # for course in course_cards:
    #      print(course)

    # return the h5 tag present inside the div tag
    # for course in course_cards:
    #     print(course.h5)

    # return the h5 tag's text present inside the div tag (Which is the names of courses)
    print("\n\n---- Extracting the course name and price from a html page ----\n\n")
    
    for course in course_cards:
        if course.h5 and course.a:
            course_name = course.h5.text
            course_price = course.a.text
            print(f"Course Name : {course_name}")
            print(f"Course Price: {course_price}")
        print()
    
        
    
    print()
   
    