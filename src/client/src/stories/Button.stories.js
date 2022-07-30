//github.com/WebDevSimplified/storybook-react-crash-course/blob/main/src/stories/Button.stories.js
import Button from "../components/atoms/button/Button";

export default {
  title: "Button",
  component: Button,
  //   do funckji np handleClick jak w przycisku
  argTypes: { handleClick: { action: "handleClickLabel" } },
};

// base function, żeby przycik był interaktywny
// Template - bierze argumenty i wszystkie przekazuje do przyciksu
// coś jak przekazywanie props do button
// tę funkcję kopiuję za każdym razem gdy używam
const Template = (args) => <Button {...args} />;

// story o nazwie Red
// http://localhost:6006/?path=/story/button--red
// bez funckji żadnych przycisk
// export const Red = () => <Button label="Press me" backgroundColor="red" />;
// przycisk z funkcjami
export const Red = Template.bind({});
Red.args = {
  backgroundColor: "red",
  label: "Press Me",
  size: "md",
};

// multiple stories
export const Green = Template.bind({});
Green.args = {
  backgroundColor: "green",
  label: "Press Me",
  size: "md",
};

export const Small = Template.bind({});
Small.args = {
  backgroundColor: "green",
  label: "Press Me",
  size: "sm",
};

export const Large = Template.bind({});
Large.args = {
  backgroundColor: "green",
  label: "Press Me",
  size: "lg",
};

export const LongLabel = Template.bind({});
LongLabel.args = {
  backgroundColor: "green",
  label: "Press Me bardzo długi label długi label długi labeldługi label",
  size: "md",
};
