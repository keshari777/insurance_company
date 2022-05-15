import React, { useEffect, useState } from "react";
import { Table, Input, Button, Modal, message } from "antd";
import { useQuery, useLazyQuery, useMutation } from "@apollo/client";
import { GET_ALL_POLICY_DETAIL, GET_POLICY_BY_ID } from "../services/queries";
import { SearchOutlined } from "@ant-design/icons";
import { UPDATE_PREMIUM_OF_POLICY } from "../services/mutations";
import { useNavigate } from "react-router-dom";

import "./PolicyComponent.css";

const PolicyComponent = () => {
  /**
   *This component is used to display table with all the policy details and has search functionality
   *with Policy Id or Customer Id
   * */
  const { data, loading } = useQuery(GET_ALL_POLICY_DETAIL, {
    fetchPolicy: "network-only",
  });
  const [getPolicyById, { data: policyData, loading: policyLoading }] =
    useLazyQuery(GET_POLICY_BY_ID);
  const [updatePolicy] = useMutation(
    UPDATE_PREMIUM_OF_POLICY,

    {
      refetchQueries: [
        {
          query: GET_ALL_POLICY_DETAIL,
        },
      ],

      onError(err) {
        message.error(err, 3);
      },
      onCompleted(data) {
        console.log("ddddd", data?.policyPremiumUpdate);
        if (data?.policyPremiumUpdate.ok) {
          message.success("Saved data successfully", 1.5);
        } else {
          message.error(data?.policyPremiumUpdate?.error);
        }
      },
    }
  );
  const [policyUpdateData, setPolicyUpdateData] = useState("");
  const [inputValue, setValue] = useState("");
  const [dataSource, setDataSource] = useState();
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [modaldata, setmodaldata] = useState([]);
  const [premiumValue, setPremeiumValue] = useState("");
  const navigate = useNavigate();

  const columns = [
    {
      title: "Policy ID",
      dataIndex: "policyId",
      width: 8,
    },
    {
      title: "Customer ID",
      dataIndex: ["customerId", "customerId"],
      width: 8,
    },
    {
      title: "Date Of Purchase",
      dataIndex: "dateOfPurchase",
      width: 8,
    },
    {
      title: "Premium",
      dataIndex: "premium",
      width: 8,
    },
    {
      title: "Vehicle Segment",
      dataIndex: "vehicleSegment",
      width: 8,
    },
    {
      title: "Fuel Type",
      dataIndex: "fuelType",
      width: 8,
    },
    {
      title: "Bodily Injury Liability",
      dataIndex: "bodilyInjuryLiability",
      width: 8,
    },
    {
      title: "Personal Injury Protection",
      dataIndex: "personalInjuryProtection",
      width: 8,
    },
    {
      title: "Property Damage Liability",
      dataIndex: "propertyDamageLiability",
      width: 8,
    },
    {
      title: "Collision",
      dataIndex: "collision",
      width: 7,
    },
    {
      title: "Comprehensive",
      dataIndex: "comprehensive",
      width: 10,
    },
    {
      title: "Edit",
      key: "id",
      dataIndex: "id",
      width: 7,
      render: (index, record) => (
        <Button type="primary" onClick={() => showModal(record)}>
          Edit
        </Button>
      ),
    },
  ];
  const showModal = (record) => {
    console.log("rrrr", record);
    setmodaldata(record);
    setIsModalVisible(true);
    setPremeiumValue(record.premium);
  };
  const searchFunction = (value) => {
    getPolicyById({
      variables: {
        id: parseInt(value),
      },
    });
  };
  useEffect(() => {
    setDataSource(data?.allPolicyDetail);
  }, [data]);

  useEffect(() => {
    setDataSource(policyData?.getPolicyById);
  }, [policyData]);

  const searchInputBox = (
    <Input
      className="search-input-box"
      placeholder="Search Policy Id or Customer Id"
      suffix={<SearchOutlined />}
      value={inputValue}
      allowClear={true}
      onChange={(e) => {
        setValue(e.target.value);
        // On click of clear button
        if (e.target.value === "") {
          setDataSource(data?.allPolicyDetail);
        }
      }}
      onPressEnter={(e) => {
        searchFunction(e.target.value);
      }}
    />
  );
  const handleCancel = () => {
    setIsModalVisible(false);
  };
  const handleOk = (e) => {
    if (e.premium !== "") {
      updatePolicy({ variables: { policyData: e } });
      setIsModalVisible(false);
    }
  };
  const openChart = () => {
    navigate("/charts");
  };
  if (loading) {
    return <p>Loading</p>;
  }

  return (
    <React.Fragment>
      <h1>Welcome to Insurance Company</h1>
      <div className="chart-container" onClick={() => openChart()}>
        Click to view Chart
      </div>
      <div className="flex-end">
        <h3>Policy Details</h3>
        {searchInputBox}
      </div>
      <Table
        className="policy-table"
        columns={columns}
        dataSource={dataSource}
        pagination={{ pageSize: 50 }}
        scroll={{ y: 240 }}
        loading={policyLoading}
      />
      <Modal
        title="Edit Policy Details"
        visible={isModalVisible}
        onOk={() => handleOk(policyUpdateData)}
        onCancel={handleCancel}
        className="edit-policy-modal"
      >
        <div className="modal-body-content">
          <p>Policy Id: {modaldata.policyId}</p>
          <p>Customer Id: {modaldata?.customerId?.customerId}</p>
          <p className="premium-detail">
            <label className="premium-label">Premium (in INR):</label>
            <Input
              className="premium-value"
              value={premiumValue}
              onChange={(e) => {
                setPremeiumValue(e.target.value);
                setPolicyUpdateData({
                  policyId: modaldata.policyId,
                  premium: e.target.value,
                });
                if (e.target.value === "") {
                  message.error("Premium value can not be Empty");
                }
              }}
            ></Input>
          </p>
        </div>
      </Modal>
    </React.Fragment>
  );
};

export default PolicyComponent;
