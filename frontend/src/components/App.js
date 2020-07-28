import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  render() {
      return (<div>EBE</div>);
  }
}


const container = document.getElementById("app");
render(<App />, container);