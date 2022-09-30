const RadioButton = ({
  className,
  groupName,
  id,
  value,
  label,
  onChange,
  checked,
}) => {
  return (
    <div className={`radio-button ${className}`}>
      <input
        className="radio-button__input"
        type="radio"
        name={groupName}
        id={id}
        value={value}
        checked={checked}
        onChange={onChange}
      />
      <label className="radio-button__label" htmlFor={id}>
        {label}
      </label>
    </div>
  );
};

export default RadioButton;
