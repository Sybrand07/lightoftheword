document.addEventListener('DOMContentLoaded', function() {
    // Handle tab switching
    document.querySelectorAll('.tab-button').forEach(button => {
        button.addEventListener('click', function() {
            const tabId = this.getAttribute('data-tab');

            // Remove active class from all tabs and contents
            document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

            // Add active class to the clicked tab and associated content
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });

    
});

function loadProducts() {
    const products = {
        posters: [
            { name: 'Grace Poster', img: '../static/images/1.jpg', description: 'Grace-themed art' },
            { name: 'Faith Poster', img: '../static/images/3.jpg', description: 'Faith-themed art' }
        ],
        canvasses: [
            { name: 'Hope Canvas', img: '../static/images/2.jpg', description: 'Hope-themed canvas' },
            { name: 'Love Canvas', img: '../static/images/4.jpg', description: 'Love-themed canvas' }
        ],
        scriptures: [
            { name: 'Psalm 23', img: 'https://via.placeholder.com/300x400', description: 'Psalm 23 artwork' },
            { name: 'John 3:16', img: 'https://via.placeholder.com/300x400', description: 'John 3:16 artwork' }
        ]
    };

    // Append products dynamically to each grid
    appendProductsToGrid('posters', products.posters);
    appendProductsToGrid('canvasses', products.canvasses);
    appendProductsToGrid('scriptures', products.scriptures);
}

function appendProductsToGrid(gridId, products) {
    const grid = document.getElementById(gridId);
    grid.innerHTML = ''; // Clear the grid before adding products

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product');
        productDiv.innerHTML = `
            <img src="${product.img}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
        `;
        grid.appendChild(productDiv);
    });
}
