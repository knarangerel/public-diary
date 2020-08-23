import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      diary: {},
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("today/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            diary: data[0],
            loaded: true
          };
        });
        console.log(data[0])
      });
  }

  render() {
    return (
      <div>
      <h3>{this.state.diary.date} - {this.state.diary.in_couple_words}</h3>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);