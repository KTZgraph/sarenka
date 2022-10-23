import { useState } from "react";

const FormInput = (props) => {
  const [focused, setFocused] = useState(false);
  const handleFocus = (e) => {
    setFocused(true);
  };

  const {
    className,
    label,
    errorMessage,
    onChange,
    id,
    nameFocus,
    ...inputProps
  } = props;
  return (
    <div className={`form-input ${className}`}>
      <label className="form-input__label">{label}</label>
      <input
        className="form-input__input"
        {...inputProps}
        onChange={onChange}
        onBlur={handleFocus}
        focused={focused.toString()}
        onFocus={() => inputProps.name === nameFocus && setFocused(true)}
      />
      <span className="form-input__error-message">{errorMessage}</span>
    </div>
  );
};

export default FormInput;
