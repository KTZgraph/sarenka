import React from 'react';
import styled from 'styled-components';
import theme from 'theme/theme';
import Input from 'components/atoms/Input/Input';

const StyledLabel = styled.label`
  display: block;
  color: ${theme.colors.font};
  font-weight: ${theme.font.weight.regular};
  margin-bottom: 7px;
`;

const StyledInput = styled(Input)`
  max-width: 300px;
  margin-bottom: 20px;
`;

type Props = {
  label: string;
  placeholder: string;
  name: string;
  defaultValue?: string;
  onChange: (
    event:
      | React.ChangeEvent<HTMLInputElement>
      | React.FocusEvent<HTMLInputElement>,
  ) => void;
};

const InputWithLabel: React.FC<Props> = ({
  label,
  placeholder,
  name,
  onChange,
  defaultValue,
}: Props) => (
  <>
    <StyledLabel htmlFor={name}>{label}</StyledLabel>
    <StyledInput
      type="text"
      id={name}
      placeholder={placeholder}
      noBorder
      onChange={onChange}
      onBlur={onChange}
      defaultValue={defaultValue}
    />
  </>
);

export default InputWithLabel;
