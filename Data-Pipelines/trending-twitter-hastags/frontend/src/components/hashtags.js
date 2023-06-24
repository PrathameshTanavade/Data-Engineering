
import React from 'react'

function HashtagItem(props) {
    
    return (


            <tr>
                <td>{props.hashtag.hashtag}</td>
                <td>{props.hashtag.count}</td>
            </tr>
                
    )
}

export default HashtagItem;