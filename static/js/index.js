// team Task 8
let backButton = document.getElementById("prev");
let nextButton = document.getElementById("next");
let parentElement = document.getElementById("books");
let messageElement = document.getElementById("message");

function renderOneItem(data) {
    const book = document.createElement("div");
    //
    book.innerHTML =
        `<div class="card h-100" style="width: 16rem;">        
        <img id="thumbnail" src="${data.volumeInfo.imageLinks.smallThumbnail}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">${data.volumeInfo.title}</h5>
          <h6 class="card-subtitle mb-2 text-muted">${data.volumeInfo.publisher}</h6>
          <p class="card-text">${data.volumeInfo.publishedDate}</p>
          <a href="#" class="card-link">Card link</a>          
        </div>
      </div>`;

    return book;
}

function renderList(parent, books) {
    books.forEach((book) => {
        parentElement.appendChild(renderOneItem(book));
    });
}

async function getAllBooks(urlSource) {
    const list = fetch(urlSource);

    list
        .then((response) => response.json())
        .then((data) => {
            //messageElement.innerHTML = `Data Elements found:<p>${JSON.stringify(data)}</p>`;

            if (data.items != undefined) {
                // alert("data results is defined, rendering data");
                renderList(parentElement, data.items);
            } else {
                alert("data results is undefined");
            }

            if (data.previous != undefined) {
                backButton.onclick = function() {
                    let prevURL = data.previous;
                    parentElement.innerHTML = "";
                    getAllBooks(prevURL)
                };
            }
            if (data.next != undefined) {
                nextButton.onclick = function() {
                    let nextURL = data.next;
                    parentElement.innerHTML = "";
                    getAllBooks(nextURL)
                };
            }
        });
}

//alert('JS loading data');

let urlBasePath = "https://www.googleapis.com/books/v1/volumes?q=Python&maxResults=10&startIndex=0";
getAllBooks(urlBasePath);