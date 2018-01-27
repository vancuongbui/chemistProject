import React from "react"
import {render} from "react-dom"
var ProductComponent = React.createClass({
    render: function() {
        var testStyle = {
            fontSize: '18px', marginRight: '20px', color: 'Red'
        };
        return (
            <div className='testClass'>
                <div style = {testStyle}>Test this string </div>                
            </div>
        )
    }
});

React.render(
    <ProductComponent/>,
    document.getElementById('testReact')
)