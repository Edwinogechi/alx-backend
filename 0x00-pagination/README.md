0x00 Pagination
Overview
0x00 Pagination is a lightweight JavaScript library designed to simplify the implementation of pagination functionality in web applications. With this library, developers can easily integrate pagination features into their projects to enhance user experience when dealing with large datasets or lists.

Features
Simple Integration: Easily integrate pagination functionality into your web application with minimal setup.
Customizable: Customize pagination styles, such as page numbers, next and previous buttons, and page size.
Responsive Design: Pagination elements adapt to various screen sizes and devices, ensuring a consistent user experience across different platforms.
Efficient Handling: Efficiently handle large datasets or lists by dividing them into smaller, manageable pages.
Installation
To install 0x00 Pagination, simply include the JavaScript file in your project:

html
Copy code
<script src="0x00-pagination.js"></script>
Usage
Initialize the pagination:
javascript
Copy code
var pagination = new Pagination({
    totalItems: 1000,
    itemsPerPage: 10,
    currentPage: 1,
    onPageChange: function(page) {
        // Handle page change event
        console.log("Page changed to: " + page);
    }
});
Add the pagination HTML element to your page:
html
Copy code
<div id="pagination"></div>
Render the pagination:
javascript
Copy code
pagination.render('pagination');
Options
totalItems: Total number of items to paginate.
itemsPerPage: Number of items to display per page.
currentPage: Current page to display.
onPageChange: Callback function to handle page change events.
Customization
You can customize the pagination by modifying the CSS styles or by passing additional options to the Pagination constructor.

Example
Check out the example directory for a simple example of how to use 0x00 Pagination in your web application.

License
0x00 Pagination is licensed under the MIT License. See the LICENSE file for details.

Contributors
Edwin Ogechi edwinogechi96@gmail.com


Tasks
0. Simple helper function

Write a function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

1. Simple pagination
Copy index_range from the previous task and the following class into your code

Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should be returned.


2. Hypermedia pagination


Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.


3. Deletion-resilient hypermedia pagination

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

Start 3-hypermedia_del_pagination.py with this code:

Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.

The method should return a dictionary with the following key-value pairs:
index: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
next_index: the next index to query with. That should be the index of the first item after the last item on the current page.
page_size: the current page size
data: the actual page of the dataset
Requirements/Behavior:

Use assert to verify that index is in a valid range.
If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.
