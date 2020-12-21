import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import ListWrapper from 'components/atoms/List/ListWrapper';
import ListItem from 'components/atoms/List/ListItem';
import NoData from 'components/atoms/NoDataText/NoDataText';

const StyledCardWrapper = styled(CardWrapper)`
  column-count: 2;
  @media (max-width: 1360px) {
    column-count: 2;
  }
  @media (max-width: 850px) {
    column-count: 1;
  }
`;

type Props = {
  tlsData: Record<string, any>;
};

const TLSInfo: React.FC<Props> = ({ tlsData }: Props) => {
  return (
    <StyledCardWrapper>
      <Paragraph wordBreak>
        {`Tbs noct fingerprint: `}
        {tlsData.tbs_noct_fingerprint?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Subject DN: `}
        {tlsData.subject_dn || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Common name: `}
        {tlsData.common_name?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Organization: `}
        {tlsData.organization?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Organizational unit: `}
        {tlsData.organizational_unit?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Signature algorithm oid : `}
        {tlsData.signature_algorithm_oid || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Signature algorithm name: `}
        {tlsData.signature_algorithm_name || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Redacted: `}
        {tlsData.redacted?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Serial number: `}
        {tlsData.serial_number || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Validation level: `}
        {tlsData.validation_level || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Issuer DN: `}
        {tlsData.issuer_dn || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Fingerprint SHA1: `}
        {tlsData.fingerprint_sha1 || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Version: `}
        {tlsData.version || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Fingerprint SHA256: `}
        {tlsData.fingerprint_sha256 || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`TBS fingerprint: `}
        {tlsData.tbs_fingerprint || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Names: `}
        {tlsData.names || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Validity start: `}
        {tlsData.validity_start || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Validity valid: `}
        {tlsData.validity_valid || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Validity start: `}
        {tlsData.validity_value || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Fingerprint MD5: `}
        {tlsData.fingerprint_md5 || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Spki subject fingerprint: `}
        {tlsData.spki_subject_fingerprint || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Subject key info fingerprint SHA256: `}
        {tlsData.subject_key_info_fingerprint_sha256 || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Subject key info fingerprint algorithm name: `}
        {tlsData.subject_key_info_key_algorithm_name || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Subject key info fingerprint RSA public key length: `}
        {tlsData.subject_key_info_rsa_public_key_lenght || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Subject key info fingerprint RSA public key modulus: `}
        {tlsData.subject_key_info_rsa_public_key_modulus || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Subject key info fingerprint RSA public key exponent: `}
        {tlsData.subject_key_info_rsa_public_key_exponent || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Signature self signed: `}
        {tlsData.signature_self_signed?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Signature valid: `}
        {tlsData.signature_valid?.toString() || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Signature value: `}
        {tlsData.signature_value || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Issuer organizational unit: `}
        {tlsData.issuer_organizational_unit || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Issuer common name: `}
        {tlsData.issuer_common_name || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Issuer organization: `}
        {tlsData.issuer_organization || <NoData />}
      </Paragraph>
      <div>
        <Paragraph listTitle>Extensions</Paragraph>
        <ListWrapper>
          <ListItem>
            {`Authority key ID: `}
            {tlsData.extensions.authority_key_id || <NoData />}
          </ListItem>
          <ListItem>
            {`Certificate policies cps: `}
            {tlsData.extensions.certificate_policies_cps?.toString() || (
              <NoData />
            )}
          </ListItem>
          <ListItem>
            {`Certificate policies ID: `}
            {tlsData.extensions.certificate_policies_id?.toString() || (
              <NoData />
            )}
          </ListItem>
          <ListItem>
            {`Authority info access ocsp urls: `}
            {tlsData.extensions.authority_info_access_ocsp_urls?.toString() || (
              <NoData />
            )}
          </ListItem>
          <ListItem>
            {`Authority info access issuer urls: `}
            {tlsData.extensions.authority_info_access_issuer_urls?.toString() || (
              <NoData />
            )}
          </ListItem>
          <ListItem>
            {`Client auth: `}
            {tlsData.extensions.client_auth || <NoData />}
          </ListItem>
          <ListItem>
            {`Server auth: `}
            {tlsData.extensions.server_auth || <NoData />}
          </ListItem>
          <ListItem>
            {`DNS names: `}
            {tlsData.extensions.dns_names || <NoData />}
          </ListItem>
          <ListItem>
            {`IS CA: `}
            {tlsData.extensions.is_ca?.toString() || <NoData />}
          </ListItem>
          <ListItem>
            {`CRL distribution points: `}
            {tlsData.extensions.crl_distribution_points?.toString() || (
              <NoData />
            )}
          </ListItem>
          <ListItem>
            {`Key usage key encipherment: `}
            {tlsData.extensions.key_usage_key_encipherment || <NoData />}
          </ListItem>
          <ListItem>
            {`Key usage value: `}
            {tlsData.extensions.key_usage_value || <NoData />}
          </ListItem>
          <ListItem>
            {`Key usage is digital signature: `}
            {tlsData.extensions.key_usage_is_digital_signature || <NoData />}
          </ListItem>
          <ListItem>
            {`Subject key ID: `}
            {tlsData.extensions.subject_key_id || <NoData />}
          </ListItem>
        </ListWrapper>
      </div>
    </StyledCardWrapper>
  );
};

export default TLSInfo;
