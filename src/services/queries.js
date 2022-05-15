import { gql } from "@apollo/client";

export const GET_POLICY_BY_ID = gql`
  query GetPolicyById($id: Int!) {
    getPolicyById(id: $id) {
      id
      policyId
      customerId {
        id
        customerId
      }
      dateOfPurchase
      premium
      vehicleSegment
      fuelType
      bodilyInjuryLiability
      personalInjuryProtection
      propertyDamageLiability
      collision
      comprehensive
    }
  }
`;

export const GET_ALL_POLICY_DETAIL = gql`
  query {
    allPolicyDetail {
      id
      policyId
      customerId {
        id
        customerId
      }
      dateOfPurchase
      premium
      vehicleSegment
      fuelType
      bodilyInjuryLiability
      personalInjuryProtection
      propertyDamageLiability
      collision
      comprehensive
    }
  }
`;

export const GET_POLICY_PER_MONTH = gql`
  query GetPolicyPerMonth($filtering: PolicyPerMonthFilterInput) {
    getPolicyPerMonth(filtering: $filtering) {
      month
      count
    }
  }
`;
