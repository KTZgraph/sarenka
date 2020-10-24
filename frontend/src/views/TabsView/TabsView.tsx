import React from 'react';
import Tab from 'components/atoms/Tab/Tab';
import { useHistory } from 'react-router';
import { useDispatch, useSelector } from 'react-redux';
import { removeTab } from 'actions/TabsActions';
import styled from 'styled-components';

const StyledTabs = styled.div`
  overflow-y: scroll;
  width: 100%;
  height: calc(100vh - 450px);

  ::-webkit-scrollbar {
    width: 0;
    background: transparent;
  }
`;

const ScrollableTabButtons = () => {
  const [newTabIndex, setNewTabIndex] = React.useState(0);
  const history = useHistory();
  const allTabs = useSelector(({ tabs }: Record<string, any>) => tabs);
  const dispatch = useDispatch();

  const handleChange = (
    event: React.ChangeEvent<{}>,
    tabIndex: number,
    location: string,
  ) => {
    setNewTabIndex(tabIndex);
    history.push(`/tabs/${tabIndex}${location}`);
  };

  const removeTabOnClick = (index: number) => {
    if (Object.keys(allTabs).length > 1) {
      dispatch(removeTab(index));
      if (newTabIndex === index) {
        const lastTab = Object.keys(allTabs).pop();
        if (lastTab) {
          const redirectTab = allTabs[lastTab];
          setNewTabIndex(redirectTab.index);
          history.push(`/tabs/${redirectTab.index}${redirectTab.link}`);
        }
      }
    }
  };

  return (
    <StyledTabs>
      {Object.keys(allTabs).map((element) => {
        const tab = allTabs[element];
        return (
          <Tab
            key={tab.index}
            label={tab.label}
            index={tab.index}
            isActive={tab.index === newTabIndex}
            onClick={(event: React.ChangeEvent<{}>) =>
              handleChange(event, tab.index, tab.link)}
            onRemoveClick={() => {
              removeTabOnClick(tab.index);
            }}
          />
        );
      })}
    </StyledTabs>
  );
};

export default ScrollableTabButtons;
