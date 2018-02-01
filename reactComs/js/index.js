import React, { Component } from 'react';

import ReactDOM from 'react-dom';



class App extends React.Component {
render() {
    return (
    <div >
        <h1>The Home page will be processed by React </h1>
        <h3>Next step, the content of page will be render by React</h3>
        <h3>React also will try to access SQLite3 database created by Django</h3>
    </div>);
}
}
ReactDOM.render(<App />, document.getElementById('react-app'));