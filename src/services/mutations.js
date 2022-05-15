import { gql } from "@apollo/client";

export const UPDATE_PREMIUM_OF_POLICY = gql`
  mutation PolicyUpdate($policyData: UpdatePolicyInput) {
    policyPremiumUpdate(policyData: $policyData) {
      ok
      error
    }
  }
`;
