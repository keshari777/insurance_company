import React, { useState, useEffect } from "react";
import { useLazyQuery, useQuery } from "@apollo/client";
import { GET_POLICY_PER_MONTH } from "../services/queries";
import Visualization from "./VisualizationGraph";
import { Select } from "antd";
import "./Analytics.css";

const PolicyPerMonth = () => {
  /**
   *This component is used to display filter with charts
   * */
  const { data, loading } = useQuery(GET_POLICY_PER_MONTH, {
    fetchPolicy: "network-only",
  });
  const [getPolicyPerMonthWithFilter, { data: policyData }] =
    useLazyQuery(GET_POLICY_PER_MONTH);

  const [dataSource, setDataSource] = useState();
  const { Option } = Select;

  useEffect(() => {
    setDataSource(data?.getPolicyPerMonth);
  }, [data]);

  useEffect(() => {
    setDataSource(policyData?.getPolicyPerMonth);
  }, [policyData]);

  function handleChange(value) {
    console.log(`selected ${value}`);
    getPolicyPerMonthWithFilter({
      variables: { filtering: { region: value } },
    });
  }

  if (loading) {
    return <p>Loading</p>;
  }
  return (
    <>
      <h1>Visualization Graph for number of policies bought in every month</h1>
      <Select
        mode="multiple"
        className="region-select"
        placeholder="Select Region"
        onChange={handleChange}
        optionLabelProp="label"
      >
        <Option value="E" label="East">
          <div className="demo-option-label-item">East</div>
        </Option>
        <Option value="W" label="West">
          <div className="demo-option-label-item">West</div>
        </Option>
        <Option value="N" label="North">
          <div className="demo-option-label-item">North</div>
        </Option>
        <Option value="S" label="South">
          <div className="demo-option-label-item">South</div>
        </Option>
      </Select>

      {dataSource && <Visualization data={dataSource} />}
    </>
  );
};
export default PolicyPerMonth;
