const DarkModeReducer = (state, action) => {
  //action.type reprezentuje nazwę funkcji
  switch (action.type) {
    case "LIGHT": {
      return {
        darkMode: false,
      };
    }
    case "DARK": {
      return {
        darkMode: true,
      };
    }
    case "TOOGLE": {
      // do księżyca tylko przełączanie
      return {
        darkMode: !state.darkMode,
      };
    }
    default:
      return state;
  }
};

export default DarkModeReducer;
