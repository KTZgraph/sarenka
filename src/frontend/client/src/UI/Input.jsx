const Input = ({ className, htmlFor, type, name, value, onChange }) => {
  return (
    <div className={`input ${className}`}>
      <label className="input__label" htmlFor={htmlFor}>
        {name}:
      </label>
      <input
        className="input__value"
        type={type}
        id={htmlFor}
        name={htmlFor}
        value={value}
        onChange={onChange}
      />
    </div>
  );
};

export default Input;
