# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Exceptions related to the IBM Quantum API."""

from ..exceptions import IBMError


class ApiError(IBMError):
    """Generic IBM Quantum API error."""

    pass


class RequestsApiError(ApiError):
    """Exception re-raising a RequestException."""

    def __init__(self, message: str, status_code: int = -1):
        """RequestsApiError constructor.

        Args:
            message: Exception message.
            status_code: Response status code. -1 for unknown status code.
        """
        super().__init__(message)
        self.status_code = status_code


class AuthenticationLicenseError(ApiError):
    """Exception due to user not having accepted the license agreement."""

    pass


class ApiIBMProtocolError(ApiError):
    """Exception related to IBM Quantum API protocol error."""

    pass


class UserTimeoutExceededError(ApiError):
    """Exceptions related to exceeding user defined timeout."""

    pass
