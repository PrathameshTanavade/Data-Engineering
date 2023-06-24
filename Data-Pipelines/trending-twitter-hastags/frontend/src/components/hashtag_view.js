
import HashtagItem from "./hashtags"

export default function HashtagsView(props) {
    return (
        <div>
            <h4 style={{marginBottom:'3em'}}>Latest trends in the city</h4>
            <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th><h5>Hashtag</h5></th>
                        <th><h5>Count</h5></th>
                    </tr>
                </thead>
                <tbody>            
                {props.hashtagList.map(hashtag => <HashtagItem hashtag={hashtag} />)}
                </tbody>
            </table>
        </div>
        </div>
    )
}