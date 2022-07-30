//github.com/WebDevSimplified/storybook-react-crash-course/blob/main/src/stories/Button.stories.js
import Stack from "../components/atoms/Stack";

export default {
  title: "Components/Atoms/Stack",
  component: Stack,
  //  nie przejmuje sie funkcjami bo jest nieklikalny
  //   argTypes: { handleClick: { action: "handleClickLabel" } },
  //   bo opakowuje dizeci
  argTypes: {
    // defaultowo 4 dzieci ten argument dzieck ajest potrzebny tylko w story book
    numberOfChildren: { type: "number", defaultValue: 4 },
  },
};

const Template = ({ numberOfChildren, ...args }) => (
  <Stack {...args}>
    {/* dla każdego numeru dziecka */}
    {[...Array(numberOfChildren).keys()].map((n) => (
      <div
        style={{
          width: "50px",
          height: "50px",
          backgroundColor: "red",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        {n + 1}
      </div>
    ))}
  </Stack>
);

// stories
export const Horizontal = Template.bind({});
Horizontal.args = {
  direction: "row",
  spacing: 2,
  wrap: false,
};

export const Vertical = Template.bind({});
Vertical.args = {
  direction: "column",
  spacing: 2,
  wrap: false,
};

export const NoSpacing = Template.bind({});
NoSpacing.args = {
  direction: "row",
  spacing: 0,
  wrap: false,
};

export const WrapOverflow = Template.bind({});
WrapOverflow.args = {
  numberOfChildren: 40,
  direction: "row",
  spacing: 2,
  wrap: true,
};

export const Empty = Template.bind({});
Empty.args = {
  numberOfChildren: 0,
  direction: "row",
  spacing: 2,
  wrap: true,
};
