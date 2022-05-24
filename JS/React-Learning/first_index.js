// ReactDOM.render(<h1 className= "header">Hello, Everyone</h1>, document.getElementById("root"))
// ReactDOM.render(<p>Hi, my name is Favour</p>, document.getElementById("root"))

// function Content(){
//     return(
//         <h1>Just seeing how to make a component</h1>
//     )
// }
// ReactDOM.render(
//     <div><Content /></div>, document.getElementById("root")
// )

// const h1 = document.createElement("h1")
// h1.textContent = "This is an imperative way to program"
// h1.className = "header"
// document.getElementById("root").append(h1)

/* JSX: is a way to write HTML in JavaScript */
// ReactDOM.render(
//     <h1>THIS WILL RESULT IN AN ERROR</h1><p>React doesn't like this, you gotta wrap it</p><p/>,
//     document.getElementById("root")
// )

// ReactDOM.render(
//     <div><h1>FIX TO LINE 19</h1><p>This is now wrapped in the div</p><p/></div>,
//     document.getElementById("root")
// )

// const page = (
//     <div>
//         <h1 className="head"> This is JSX</h1>
//         <p>This is a paragraph</p>
//     </div>
// )

// ReactDOM.render(
//     page,
//     document.getElementById("root")
// )
// console.log(page)

const navbar = (
    <nav>
        <h1> Bob's Burgers</h1>
        <ul>
            <li>Menu</li>
            <li>About</li>
            <li>Contact</li>
        </ul>
    </nav>
)

ReactDOM.render(navbar, document.getElementById("root"))