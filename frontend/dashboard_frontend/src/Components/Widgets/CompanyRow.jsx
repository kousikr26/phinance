import React, { useEffect } from 'react'
import { useState } from 'react';
import { useDispatch } from "react-redux";
import IconButton from '@mui/material/IconButton';
import BookmarkBorderIcon from '@mui/icons-material/BookmarkBorder';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import './table.scss';
import { getMetricsFromFiling, getKeyMetricOfCompany } from '../../actions/action';

const CompanyRow = (props) => {
    const dispatch = useDispatch();
    const [hasCheckbox, setHasCheckbox] = useState(props.hasCheckbox);
    const [isCompany, setIsCompany] = useState(props.isCompany);
    const filings = props.filing.filings;

    const [ARR, setARR] = useState("");
    const [CCR, setCCR] = useState("");
    const [LTV, setLTV] = useState("");
    const [CAC, setCAC] = useState("");
    const [ARPA, setARPA] = useState("");
    const [RCC, setRCC] = useState("");

    const [hover, setHover] = useState(false);
    const [hoverbg, setHoverBg] = useState(false);
    const handleMouseIn = () => {
        setHover(true);
    }
    const handleMouseOut = () => {
        setHover(false);
    }
    const handleMouseInBg = () => {
        setHoverBg(true);
    };
    const handleMouseOutBg = () => {
        setHoverBg(false);
    };
    return (
        <>
            {
                filings.map((filing, i) => {
                    const key_metrics = filing.key_metrics||[];
                    let ARR, CCR, LTV, CAC, ARPA, RCC;

                    for(let i=0;i<key_metrics.length;i++){
                        // console.log("I", key_metrics[i])
                        if(key_metrics[i]['metric_type']=="ARR"){
                            ARR=key_metrics[i]['metric_value']
                        }
                        else if(key_metrics[i]['metric_type']=="CCR"){
                            CCR=key_metrics[i]['metric_value']
                        }
                        else if(key_metrics[i]['metric_type']=="LTV"){
                            LTV=key_metrics[i]['metric_value']
                        }
                        else if(key_metrics[i]['metric_type']=="CAC"){
                            CAC=key_metrics[i]['metric_value']
                        }
                        else if(key_metrics[i]['metric_type']=="ARPA"){
                            ARPA=key_metrics[i]['metric_value']
                        }
                        else if(key_metrics[i]['metric_type']=="RCC"){
                            RCC=key_metrics[i]['metric_value']
                        }
                        
                    }
                    return (
                        <div className={hoverbg ? "listing ishover" : "listing"} onMouseOver={handleMouseInBg} onMouseLeave={handleMouseOutBg}>
                            <div className="listingheader-wrapper">

                                <div class={hasCheckbox ? "listingheadergrid hascheckbox" : "listingheadergrid"}>

                                    {hasCheckbox && <div className="actiondiv">
                                        <input className='checkbox' type="checkbox" />
                                    </div>}

                                    <>
                                        <div class="filingcontainer">
                                            <div class="ui-text issecondarybutton isfiling">{filing['company_id']}</div>
                                        </div>
                                    </>
                                </div>
                            </div>
                                <div className="div-block-4">
                                    <h4 id="w-node-_5f9bbd68-5925-7f41-4e08-47c4097194e4-5d4911ed" className="iscolumn black50">{ARR?ARR:'-'}</h4>
                                    <h4 id="w-node-_5f9bbd68-5925-7f41-4e08-47c4097194e6-5d4911ed" className="iscolumn black50">{CCR?CCR:'-'}</h4>
                                    <h4 id="w-node-_5f9bbd68-5925-7f41-4e08-47c4097194e8-5d4911ed" className="iscolumn green">{LTV?LTV:'-'}</h4>
                                    <h4 id="w-node-_5f9bbd68-5925-7f41-4e08-47c4097194ea-5d4911ed" className="iscolumn red">{CAC?CAC:'-'}</h4>
                                    <div onMouseOver={handleMouseIn} onMouseLeave={handleMouseOut} className="actions">
                                        <div className={hover ? "actioncontainer " : "actioncontainer hide"}>
                                            <IconButton style={{ backgroundColor: 'transparent' }} aria-label="delete">
                                                <BookmarkBorderIcon />
                                            </IconButton>
                                        </div>
                                        <div className={hover ? "actioncontainer " : "actioncontainer hide"}>
                                            <IconButton style={{ backgroundColor: 'transparent' }} aria-label="delete">
                                                <BookmarkBorderIcon />
                                            </IconButton>
                                        </div>
                                        <div className={hover ? "actioncontainer " : "actioncontainer hide"}>
                                            <IconButton style={{ backgroundColor: 'transparent' }} aria-label="delete">
                                                <BookmarkBorderIcon />
                                            </IconButton>
                                        </div>
                                        <div className={!hover ? "actioncontainer " : "actioncontainer hide"}>
                                            <MoreVertIcon />
                                        </div>
                                    </div>
                                </div>

                        </div>
                    );
                })}
        </>
    )
}

export default CompanyRow;