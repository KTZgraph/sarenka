import React, { useEffect } from 'react';
import Tab from 'components/atoms/Tab/Tab';
import { useHistory, useParams } from 'react-router';
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
  const history = useHistory();
  const allTabs = useSelector(({ tabs }: Record<string, any>) => tabs);
  const dispatch = useDispatch();
  const page = window.location.href.split('/')[4];
  const [newTabIndex, setNewTabIndex] = React.useState(Number(0));

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
          history.push(`/tabs/${redirectTab.index}${redirectTab.link}`);
        }
      }
    }
  };

  useEffect(() => {
    const currentTabIndex = allTabs[page]
      ? allTabs[page].index
      : allTabs[Object.keys(allTabs)[0]].index;
    setNewTabIndex(currentTabIndex);
  }, [allTabs, page]);

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
