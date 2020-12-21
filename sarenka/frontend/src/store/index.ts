import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import cveSearchReducer from 'reducers/cveSearchReducer';
import registryScanReducer from 'reducers/registryScanReducer';
import remoteHostReducer from 'reducers/remoteHostReducer';
import hardwareInfoReducer from 'reducers/hardwareInfoReducer';
import tabsReducer from 'reducers/TabsReducer';
import storage from 'redux-persist/lib/storage';
import { persistStore, persistReducer } from 'redux-persist';

declare global {
  interface Window {
    __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: typeof compose;
  }
}

const persistConfig = {
  key: 'root',
  storage,
};

const rootReducer = combineReducers({
  cveSearch: cveSearchReducer,
  registryScan: registryScanReducer,
  remoteHost: remoteHostReducer,
  hardwareInfo: hardwareInfoReducer,
  tabs: tabsReducer,
});

const persistedReducer = persistReducer(persistConfig, rootReducer);

/* eslint-disable no-underscore-dangle */
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  persistedReducer,
  composeEnhancers(applyMiddleware(thunk)),
);
/* eslint-enable */

export const persist = persistStore(store);
export default store;
