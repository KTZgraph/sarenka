const Dropdown = ({ className, label, value, options, onChange }) => {
  return (
    <div className={`dropdown ${className}`}>
      <label className="dropdown__label">
        <span className="dropdown__title">{label}:</span>
        <select
          className="dropdown__list-option"
          value={value}
          onChange={onChange}
        >
          {options.map((option, idx) => (
            <option key={idx} className="dropdown__option" value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </label>
    </div>
  );
};
export default Dropdown;
