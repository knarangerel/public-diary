import React, { useState, useEffect } from "react";
import { render } from "react-dom";

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
  },
  titleText: {
    fontFamily: "sans-serif",
    fontSize: 20,
    margin: 50,
  },
  descriptionText: {
    fontFamily: "sans-serif",
    fontSize: 18,
    padding: 15,
    margin: 0,
    // backgroundColor: "yellow",
  },
  entryText: {
    fontFamily: "sans-serif",
    fontSize: 18,
    padding: 15,
    margin: 0,
    // backgroundColor: "blue",
    lineHeight: 1,
  },
  adjText: {
    fontFamily: "sans-serif",
    fontSize: 18,
    paddingLeft: 15,
    margin: 0,
    marginTop: 6,
  },
};

const EntryDescription = ({ emoji, checkedIn, trueText, falseText }) => {
  return (
    <>
      {checkedIn ? (
        <p style={styles.descriptionText} role="img">
          {emoji}
          {trueText}
        </p>
      ) : (
        <p style={styles.descriptionText} role="img">
          {emoji}
          {trueText}
        </p>
      )}
    </>
  );
};

function App() {
  const [diary, setDiary] = useState({
    date: "",
    caption: "",
    rating: 0,
    adjectives: [],
  });
  const [checkedIn, setCheckedIn] = useState(true);

  async function fetchDiary() {
    try {
      let response = await fetch("today/");
      if (response.status > 400) {
        setCheckedIn(false);
        response = await fetch("lastavailable/");
      }
      const json = await response.json();
      setDiary({ ...json[0] });
    } catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchDiary();
  }, []);

  return (
    <div style={styles.container}>
      {checkedIn ? (
        <span style={styles.titleText} role="img">
          👋{" Hello! Thank you for checking in with me! "}😊
        </span>
      ) : (
        <span style={styles.titleText} role="img">
          {"I have not checked in today. "}🤦‍♀️
          {"  Please check back later! "}😊
        </span>
      )}
      <table>
        <tr>
          <td valign="top">
            <EntryDescription
              emoji=" 📅 "
              checkedIn={checkedIn}
              trueText="What is the date today? "
              falseText="The most recent entry is for: "
            />
          </td>
          <td>
            <p style={styles.entryText}>🍰 {diary.date}</p>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <EntryDescription
              emoji=" 💬 "
              checkedIn={checkedIn}
              trueText="How is my day going? "
              falseText="Caption of the day: "
            />
          </td>
          <td>
            <p style={styles.entryText}>🐘 {diary.caption}</p>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <EntryDescription
              emoji=" 🤔 "
              checkedIn={checkedIn}
              trueText="If I were to rate my day: "
              falseText="Rating of the day: "
            />
          </td>
          <td>
            <p style={styles.entryText}>🌻 {diary.rating}/10</p>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <EntryDescription
              emoji=" 🤪 "
              checkedIn={checkedIn}
              trueText="How am I feeling? "
              falseText="Adjectives of the day: "
            />
          </td>
          <td>
            {diary.adjectives.map((adj) => (
              <span key={adj} style={styles.adjText}>
                💠 {adj}
              </span>
            ))}
          </td>
        </tr>
      </table>
    </div>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
