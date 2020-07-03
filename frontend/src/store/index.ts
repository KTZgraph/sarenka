import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import cveSearchReducer from 'reducers/cveSearchReducer';
import registryScanReducer from 'reducers/registryScanReducer';
import remoteHostReducer from 'reducers/remoteHostReducer';

declare global {
  interface Window {
    __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: typeof compose;
  }
}

const rootReducer = combineReducers({
  cveSearch: cveSearchReducer,
  registryScan: registryScanReducer,
  remoteHost: remoteHostReducer,
});

/* eslint-disable no-underscore-dangle */
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  rootReducer,
  composeEnhancers(applyMiddleware(thunk)),
);
/* eslint-enable */

export default store;
