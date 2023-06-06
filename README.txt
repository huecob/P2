This project will be a full-stack single-page React app called Bookworm.

General USERFLOW:

A user will register or log into the site. The homepage will then become a userdashboard. On the dashboard, 
users can submit books that they're currently reading, move books that they've finished, and... potentially
retire books that they haven't finished reading and probably don't intend to. Based on the books that 
a user has submitted, they'll get recommendations for similar books off the web. Users will be able to interact
with each other through private messaging and general forum style comments under a book profile.

-- 

FEATURE DETAILS:

    LOGIN/REGISTRATION:

        Logging in will require a db. It will also require quierying the db and sending back and forth through
        a front and back end. Maybe I should include OAuth on this? And hash mapping for passwords.

        What kind of details will we need on a user to register?
            - name, email, password, general location, favorite book genre

    DASHBOARD:

        The dashboard needs to have a form of some sort for users to send their reads. There should be tables:
            - Want to read
            - Started reading
            - Stopped reading
            - Finished reading
            - Advertising books
            - Messages 

        There should also be maybe some sort of small swipable window that advertises other books off a web scrape.
        If they click on the window, it should pause the marquee and show details about the book + leave comments on it.
        Users can exit out of here or they can submit it to their want to read. 

        The want to read table should allow users to click on book and search for places to find it locally or online.

        All usernames that appear in commenting or anywhere on the site should lead to the users profile. If it's another user,
        they should be able to private message them.

--

MODEL DETAILS:

    There are users, books, genres, messages.

    One user can read many books. 
    One user can have many messages.

    One book can have many users.
    One book can have many genres.
    One book can have multiple messages.

    One message can have 2 users.
    One message can have 1 book.

    One genre can have many books.

