const userDiv = document.getElementById("users");

async function load_users(){
    try{
        userDiv.innerHTML = "Loading users.....";

        const result = await fetch("https://jsonplaceholder.typicode.com/users");

        if (!result.ok){
            throw new Error(`HTTP Error : ${result.status}`);
        };

        userDiv.innerHTML = "";

        // convert this output to the js object using .json() so that js can interact with the output
        let users = await result.json();

        users = users.slice(0, 3);

        users.forEach((user) => {
            const card = document.createElement("div");

            card.innerHTML = `
            <h3>${user.name}</h3>
            <p>${user.email}</p>
            <p>${user.phone}</p>`;

            userDiv.appendChild(card);
        });}
    catch (error){
        console.log("Something went wrong", error);
        userDiv.innerHTML = `<h2>Something went wrong ${error.message}`;
    };
    
}

load_users()