import './SpinnerHeart.css'
// https://yqnn.github.io/svg-path-editor/


const SpinnerHeart = () => {
  return (
    <div className="icon">
      <svg class="heart" viewBox="0 0 512 512" width="100" title="heart">
        <path d="M0 0 75-75 187.5 0 300-75 375 0 375 150 187.5 300 0 150 0 0 0 0 0 0 0 0 0 0 0 0 5-5" />
      </svg>
      <p>Loading ...</p>
    </div>
  )
}

export default SpinnerHeart;

