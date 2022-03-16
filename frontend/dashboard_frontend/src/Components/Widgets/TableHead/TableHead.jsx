import { Button } from '@mui/material'
import React from 'react'
import FileDownloadIcon from '@mui/icons-material/FileDownload';

const TableHead = () => {
  return (
      <>
    <div style={{display:"flex",justifyContent:"space-between",width:"100%",paddingBottom:"10px"}}>
        <div>
        <Button style={{color:'black'}}>Financials</Button>
        <Button style={{color:'#9B9B9C'}}>Fillings</Button>
        </div>
        <div>
            <Button style={{color:'#9B9B9C'}}>Download CSV <FileDownloadIcon /></Button>
        </div>
        
    </div>
    <div id="w-node-_6ba67ff8-ad2b-5c1d-c70d-8afb033cbe29-5d4911ed" className="separator" style={{margin:"0px 14px"}}></div>
    </>
  )
}

export default TableHead