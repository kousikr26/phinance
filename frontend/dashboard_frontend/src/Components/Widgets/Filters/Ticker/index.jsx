import React from "react";
import '../../../../global.scss';
import './ticker.scss';
import tickerSearchEnter from "../../../../images/widgets/Tickersearchenter.svg";

const Ticker = ({handleSearchFillings}) => {
    return (
        <div id="w-node-_81d8dbc1-a99d-2a58-a2e6-ec975f1b0dc3-5d4911ed" className="filter-ticker">
            <div className="ui-text black100">Ticker</div>
            <div className="tickersearch">
                <div className="tickerinput">
                    <h4 className="black50">AMZN</h4>
                </div>
                <a href="#" className="w-inline-block">
                    <button style={{background:"transparent",padding:"0px",margin:"0px"}} onClick={()=>handleSearchFillings()}><div className="div-block-12"><img src={tickerSearchEnter} loading="lazy" alt="" /></div></button>
                </a>
            </div>
        </div>
    );
}

export default Ticker;