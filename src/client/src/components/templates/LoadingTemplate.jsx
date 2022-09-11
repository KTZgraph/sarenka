import Spinner from '../atoms/spinner/index';
import './style.scss';

const LoadingTemplate = () => {
  return (
    <div className="main__container">
      <div className="loadingContainer">
        <div className="spinnerContainer">
          <Spinner className="spinner" />
        </div>
      </div>
    </div>
  );
};

export default LoadingTemplate;
